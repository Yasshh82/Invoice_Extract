from .base import BaseProcessor

class InvoiceNumberProcessor(BaseProcessor):
    def process(self, value):
        if value is None:
            return None

        value.value = value.value.strip()

        return value