from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ExtractedField:
    label: str
    value: str
    confidence: float
    page: int | None = None
    tokens: list[str] | None = None
    bbox: list[int] | None = None


@dataclass(slots=True)
class StructuredInvoice:
    vendor_name: dict[str, Any] | None
    invoice_number: dict[str, Any] | None
    invoice_date: dict[str, Any] | None
    gst_number: dict[str, Any] | None
    total_amount: dict[str, Any] | None

    def to_dict(self) -> dict[str, dict[str, Any] | None]:
        return {
            "vendor_name": self.vendor_name,
            "invoice_number": self.invoice_number,
            "invoice_date": self.invoice_date,
            "gst_number": self.gst_number,
            "total_amount": self.total_amount,
        }