import re
from .base import BaseProcessor

GST_REGEX = re.compile(r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[A-Z0-9]{1}Z[A-Z0-9]{1}$")

class GSTProcessor(BaseProcessor):
    def process(self, value):
        if value is None:
            return None

        gst = value.value.replace(" ", "").upper()

        if not GST_REGEX.fullmatch(gst):
            return None

        value.value = gst

        return value