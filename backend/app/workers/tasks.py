from app.constants.invoice_status import InvoiceStatus
from app.core.logging import logger
from app.database.session import SessionLocal
from app.repositories.invoice_repositiory import InvoiceRepository
from app.services.document_processing import DocumentProcessingService
from app.services.invoice_persistence_service import InvoicePersistenceService

from .celery_app import celery_app

@celery_app.task(name="process_invoice",)
def process_invoice(invoice_id: int):
    db = SessionLocal()
    persistence_service = None

    try:
        repository = InvoiceRepository(db)
        invoice = repository.get(invoice_id)

        if invoice is None:
            return

        logger.info("Started processing invoice {}", invoice_id,)

        persistence_service = InvoicePersistenceService(repository=repository)
        persistence_service.update_status(invoice, InvoiceStatus.PROCESSING)

        processor = DocumentProcessingService(
            persistence_service=persistence_service
        )
        processor.process(invoice)

        persistence_service.update_status(invoice, InvoiceStatus.COMPLETED)

        logger.info("Finished processing invoice {}", invoice_id,)

    except Exception:
        logger.exception("Processing failed.")

        if invoice and persistence_service is not None:
            persistence_service.update_status(invoice, InvoiceStatus.FAILED)

    finally:
        db.close()