from app.constants.invoice_status import InvoiceStatus
from app.core.logging import logger
from app.database.session import SessionLocal
from app.repositories.invoice_repositiory import InvoiceRepository
from app.services.document_processing import DocumentProcessingService

from .celery_app import celery_app

@celery_app.task(name="process_invoice",)
def process_invoice(invoice_id: int):
    db = SessionLocal()

    try:
        repository = InvoiceRepository(db)
        invoice = repository.get(invoice_id)

        if invoice is None:
            return

        logger.info("Started processing invoice {}", invoice_id,)

        invoice.processing_status = (InvoiceStatus.PROCESSING)

        db.commit()

        processor = DocumentProcessingService()
        processor.process(invoice)

        invoice.processing_status = (InvoiceStatus.COMPLETED)

        db.commit()

        logger.info("Finished processing invoice {}", invoice_id,)

    except Exception:
        logger.exception("Processing failed.")

        if invoice:
            invoice.processing_status = (InvoiceStatus.FAILED)

            db.commit()

    finally:
        db.close()