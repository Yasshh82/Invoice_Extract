from app.models.invoice import Invoice
from app.repositories.invoice_repositiory import InvoiceRepository

BASE_URL = "http://localhost:8000"


class InvoiceService:

    def __init__(self, repository: InvoiceRepository):
        self.repository = repository

    def create_invoice(self, data):
        invoice = Invoice(**data.model_dump())
        return self.repository.create(invoice)

    def to_response(self, invoice):
        return {
            "id": invoice.id,
            "filename": invoice.filename,
            "file_url": f"{BASE_URL}/{invoice.file_path}",
            "file_size": invoice.file_size,
            "mime_type": invoice.mime_type,
            "processing_status": invoice.processing_status,
            "uploaded_at": invoice.uploaded_at,
        }

    def get_all(self):
        invoices = self.repository.get_all()
        return [self.to_response(invoice) for invoice in invoices]

    def get(self, invoice_id):
        invoice = self.repository.get(invoice_id)
        if invoice is None:
            return None
        return self.to_response(invoice)

    def delete(self, invoice_id):
        self.repository.delete(invoice_id)