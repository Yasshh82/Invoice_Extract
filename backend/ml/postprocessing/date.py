from datetime import datetime
from dateutil.parser import parse
from .base import BaseProcessor

class DateProcessor(BaseProcessor):
    def process(self, value):
        if value is None:
            return None

        try:
            date = parse(value.value, dayfirst=True)
            value.value = date.strftime("%Y-%m-%d")

        except Exception:
            return None

        return value