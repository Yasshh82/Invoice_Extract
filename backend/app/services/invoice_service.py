from app.models.invoice import Invoice
from app.repositories.invoice_repositiory import InvoiceRepository

class InvoiceService:

    def __init__(self, repository: InvoiceRepository):
        self.repository = repository

    def create_invoice(self, data):
        invoice = Invoice(**data.model_dump())
        return self.repository.create(invoice)
    
    def get_all(self):
        return self.repository.get_all()
    
    def get(self, invoice_id):
        return self.repository.get(invoice_id)
    
    def delete(self, invoice_id):
        self.repository.delete(invoice_id)