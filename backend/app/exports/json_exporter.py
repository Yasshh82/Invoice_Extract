import io
import json

from .base import ExportStrategy

class JSONExporter(ExportStrategy):

    def export(self, invoices):
        data = []

        for invoice in invoices:
            data.append(
                {
                    "filename": invoice.filename,
                    "vendor_name": invoice.vendor_name,
                    "invoice_number": invoice.invoice_number,
                    "invoice_date": invoice.invoice_date,
                    "gst_number": invoice.gst_number,
                    "total_amount": invoice.total_amount,
                }
            )

        stream = io.StringIO()

        json.dump(data, stream, indent=4)

        stream.seek(0)

        return stream