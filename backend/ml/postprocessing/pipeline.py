from .currency import CurrencyProcessor
from .date import DateProcessor
from .gst import GSTProcessor
from .invoice_number import InvoiceNumberProcessor
from .vendor import VendorProcessor

class PostProcessingPipeline:
    def __init__(self):
        self.vendor = VendorProcessor()
        self.invoice_number = InvoiceNumberProcessor()
        self.date = DateProcessor()
        self.gst = GSTProcessor()
        self.currency = CurrencyProcessor()

    def process(self, invoice):
        invoice.vendor_name = self.vendor.process(invoice.vendor_name)
        invoice.invoice_number = self.invoice_number.process(invoice.invoice_number)
        invoice.invoice_date = self.date.process(invoice.invoice_date)
        invoice.gst_number = self.gst.process(invoice.gst_number)
        invoice.total_amount = self.currency.process(invoice.total_amount)

        return invoice