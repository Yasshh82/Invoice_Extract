import uuid

from celery import group

from app.workers.tasks import process_invoice
from .tracker import BatchTracker

tracker = BatchTracker()

class BatchManager:
    def submit(self, invoice_ids):
        batch_id = str(uuid.uuid4())
        tracker.create(batch_id, len(invoice_ids))

        workflow = group(process_invoice.s(invoice_id, batch_id) for invoice_id in invoice_ids)
        workflow.apply_async()

        return batch_id