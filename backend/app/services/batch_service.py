import uuid

from app.constants.invoice_status import InvoiceStatus
from app.mappers.batch_mapper import BatchMapper

from app.models.batch_invoice import BatchInvoice
from app.models.processing_batch import ProcessingBatch

class BatchService:
    def __init__(self, repository):
        self.repository = repository

    def create(self, invoice_ids):
        batch = ProcessingBatch(id=str(uuid.uuid4()), status="processing", total=len(invoice_ids))
        self.repository.create_batch(batch)

        for invoice_id in invoice_ids:
            self.repository.create_batch_invoice(
                BatchInvoice(batch_id=batch.id, invoice_id=invoice_id, status=InvoiceStatus.PROCESSING)
            )

        return batch

    def get(self, batch_id: str):
        batch = self.repository.get_batch(batch_id)
        if batch is None:
            return None
        return BatchMapper.to_response(batch)
