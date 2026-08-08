import uuid

from celery import group

from app.database.session import SessionLocal
from app.repositories.batch_repository import BatchRepository
from app.services.batch_service import BatchService
from app.workers.tasks import process_invoice

class BatchManager:
    def submit(self, invoice_ids):
        db = SessionLocal()
        repository = BatchRepository(db)
        service = BatchService(repository)

        batch = service.create(invoice_ids)

        workflow = group(process_invoice.s(invoice_id, batch.id) for invoice_id in invoice_ids)
        workflow.apply_async()

        db.close()
        return batch.id