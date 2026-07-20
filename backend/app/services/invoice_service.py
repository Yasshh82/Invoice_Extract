from app.models.invoice import Invoice
from app.repositories.invoice_repositiory import InvoiceRepository
from app.exceptions.invoice_exceptions import InvoiceNotFoundException
from app.mappers.invoice_mapper import InvoiceMapper

class InvoiceService:

    def __init__(self, repository: InvoiceRepository):
        self.repository = repository

    def create_invoice(self, data):
        invoice = Invoice(**data.model_dump())
        return self.repository.create(invoice)

    def get(self, invoice_id):
        invoice = self.repository.get(invoice_id)
        if invoice is None:
            raise InvoiceNotFoundException()
        return InvoiceMapper.to_response(invoice)

    def get_all(self):
        invoices = self.repository.get_all()
        return InvoiceMapper.to_response_list(invoices)

    def delete(self, invoice_id):
        invoice = self.repository.get(invoice_id)
        if invoice is None:
            raise InvoiceNotFoundException()
        self.repository.delete(invoice)