from .base import BaseProcessor

class VendorProcessor(BaseProcessor):
    def process(self, value):
        if value is None:
            return None

        value.value = " ".join(value.value.split())

        return value