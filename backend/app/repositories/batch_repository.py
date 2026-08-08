from datetime import datetime

from app.models.batch_invoice import BatchInvoice
from app.models.processing_batch import ProcessingBatch

class BatchRepository:
    def __init__(self, db):
        self.db = db

    def create_batch(self, batch):
        self.db.add(batch)
        self.db.commit()
        self.db.refresh(batch)
        return batch

    def get_batch(self, batch_id):
        return self.db.get(ProcessingBatch, batch_id)

    def update_batch(self, batch):
        self.db.commit()
        self.db.refresh(batch)
        return batch

    def create_batch_invoice(self, batch_invoice):
        self.db.add(batch_invoice)
        self.db.commit()
        self.db.refresh(batch_invoice)
        return batch_invoice

    def get_batch_invoice(self, batch_id: str, invoice_id: int):
        return (
            self.db.query(BatchInvoice)
            .filter(
                BatchInvoice.batch_id == batch_id,
                BatchInvoice.invoice_id == invoice_id,
            )
            .first()
        )