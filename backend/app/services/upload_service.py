from fastapi import UploadFile

from app.batch.manager import BatchManager
from app.models.invoice import Invoice
from app.repositories.invoice_repositiory import InvoiceRepository
from app.services.file_storage import save_file
from app.constants.invoice_status import InvoiceStatus
from app.core.logging import logger
from app.mappers.invoice_mapper import InvoiceMapper
from app.workers.tasks import process_invoice


class UploadService:
    def __init__(self, repository: InvoiceRepository,):
        self.repository = repository

    def upload(self, upload_file: UploadFile,):
        logger.info("Uploading file: %s", upload_file.filename)

        try:
            invoice = self._create_invoice(upload_file)
            process_invoice.delay(invoice.id)
            logger.info("Invoice %s stored successfully", invoice.id)
            return InvoiceMapper.to_response(invoice)
        except Exception:
            logger.exception("Failed to upload file: %s", upload_file.filename)
            raise
    
    def upload_bulk(self, files: list[UploadFile],):
        invoice_ids = []

        for file in files:
            try:
                invoice = self._create_invoice(file)
                invoice_ids.append(invoice.id)
            except Exception:
                logger.warning("Skipped file in bulk upload: %s", file.filename)

        batch_id = BatchManager().submit(invoice_ids)
        return {
            "batch_id": batch_id,
            "invoice_ids": invoice_ids,
        }

    def _create_invoice(self, upload_file: UploadFile):
        file_path = save_file(upload_file)

        invoice = Invoice(
            filename=upload_file.filename,
            file_path=str(file_path),
            file_size=file_path.stat().st_size,
            mime_type=upload_file.content_type,
            processing_status=InvoiceStatus.UPLOADED,
        )

        invoice = self.repository.create(invoice)
        logger.info("Invoice %s stored successfully", invoice.id)
        return invoice