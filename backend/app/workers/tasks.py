from datetime import datetime

from app.constants.invoice_status import InvoiceStatus
from app.core.logging import logger
from app.database.session import SessionLocal
from app.repositories.batch_repository import BatchRepository
from app.repositories.invoice_repositiory import InvoiceRepository
from app.services.document_processing import DocumentProcessingService
from app.services.invoice_persistence_service import InvoicePersistenceService

from .celery_app import celery_app


@celery_app.task(name="process_invoice")
def process_invoice(invoice_id: int, batch_id: str | None = None):
    db = SessionLocal()
    persistence_service = None
    invoice = None
    success = False

    try:
        repository = InvoiceRepository(db)
        invoice = repository.get(invoice_id)

        if invoice is None:
            return

        logger.info("Started processing invoice {}", invoice_id)

        persistence_service = InvoicePersistenceService(repository=repository)
        persistence_service.update_status(invoice, InvoiceStatus.PROCESSING)

        processor = DocumentProcessingService(
            persistence_service=persistence_service
        )
        processor.process(invoice)

        persistence_service.update_status(invoice, InvoiceStatus.COMPLETED)
        success = True

        logger.info("Finished processing invoice {}", invoice_id)

    except Exception as exc:
        logger.exception("Processing failed.")

        exception = exc
        if invoice and persistence_service is not None:
            persistence_service.update_status(invoice, InvoiceStatus.FAILED)

    finally:
        if batch_id:
            batch_repo = BatchRepository(db)
            batch_invoice = batch_repo.get_batch_invoice(batch_id, invoice_id)
            batch = batch_repo.get_batch(batch_id)

            if batch_invoice is not None and batch is not None:
                if success:
                    batch_invoice.status = InvoiceStatus.COMPLETED
                    batch_invoice.completed_at = datetime.utcnow()
                    batch.completed += 1
                else:
                    batch_invoice.status = InvoiceStatus.FAILED
                    batch_invoice.error_message = str(exception) if exception is not None else "Processing failed"
                    batch.failed += 1

                if batch.completed + batch.failed == batch.total:
                    batch.finished_at = datetime.utcnow()
                    batch.status = "Completed"

                db.commit()
                db.refresh(batch_invoice)
                db.refresh(batch)

        db.close()