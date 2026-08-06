from .models import StructuredInvoice


class EntityAggregator:

    def aggregate(self, entities):

        values = {}

        for entity in entities:
            key = entity.label.lower()
            values[key] = {
                "value": entity.value,
                "confidence": entity.confidence,
                "page": entity.page,
                "tokens": entity.tokens or [],
                "bbox": entity.bbox,
            }

        return StructuredInvoice(
            vendor_name=values.get("company"),
            invoice_number=values.get("invoice_number"),
            invoice_date=values.get("date"),
            gst_number=values.get("gst"),
            total_amount=values.get("total")
        )