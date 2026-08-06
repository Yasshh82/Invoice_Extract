import re
from decimal import Decimal

from .base import BaseProcessor

class CurrencyProcessor(BaseProcessor):
    def process(self, value):
        if value is None:
            return None

        text = re.sub(r"[^\d.,]", "", value.value)

        text = text.replace(",", "")

        try:
            amount = Decimal(text)

        except Exception:
            return None

        value.value = f"{amount:.2f}"

        return value
    