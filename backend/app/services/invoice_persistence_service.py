from datetime import datetime
from decimal import Decimal
from typing import Any

from app.constants.invoice_status import InvoiceStatus
from app.repositories.invoice_repositiory import InvoiceRepository


class InvoicePersistenceService:
    def __init__(self, repository: InvoiceRepository | None = None):
        self.repository = repository

    def _extract_value(self, value):
        if isinstance(value, dict):
            return value.get("value")
        return value

    def _extract_confidence(self, value):
        if isinstance(value, dict):
            return value.get("confidence")
        return None

    def _coerce_date(self, value: str | None):
        if not value:
            return None

        try:
            from datetime import date

            return date.fromisoformat(value)
        except ValueError:
            return None

    def _coerce_decimal(self, value: str | None):
        if not value:
            return None

        try:
            return Decimal(str(value))
        except Exception:
            return None

    def _build_confidence_metadata(self, inference_result) -> dict[str, Any]:
        return {
            field_name: self._extract_confidence(getattr(inference_result, field_name, None))
            for field_name in [
                "vendor_name",
                "invoice_number",
                "invoice_date",
                "gst_number",
                "total_amount",
            ]
            if self._extract_confidence(getattr(inference_result, field_name, None)) is not None
        }

    def update_status(self, invoice, status: InvoiceStatus | str, processed_at: datetime | None = None):
        if invoice is None:
            return None

        invoice.processing_status = status
        if processed_at is not None or status in {InvoiceStatus.COMPLETED, InvoiceStatus.FAILED}:
            invoice.processed_at = processed_at or datetime.utcnow()

        if self.repository is not None:
            self.repository.update(invoice)

        return invoice

    def persist(
        self,
        invoice,
        inference_result,
        status: InvoiceStatus | str = InvoiceStatus.COMPLETED,
        confidence_metadata: dict[str, Any] | None = None,
    ):
        if invoice is None:
            return None

        invoice.vendor_name = self._extract_value(inference_result.vendor_name)
        invoice.invoice_number = self._extract_value(inference_result.invoice_number)
        invoice.invoice_date = self._coerce_date(self._extract_value(inference_result.invoice_date))
        invoice.gst_number = self._extract_value(inference_result.gst_number)
        invoice.total_amount = self._coerce_decimal(self._extract_value(inference_result.total_amount))

        invoice.processing_status = status
        invoice.processed_at = datetime.utcnow()

        metadata = confidence_metadata or self._build_confidence_metadata(inference_result)
        invoice.confidence_metadata = metadata

        if self.repository is not None:
            self.repository.update(invoice)

        return invoice
