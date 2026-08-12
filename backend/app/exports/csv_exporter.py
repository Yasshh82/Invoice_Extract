import csv
import io

from .base import ExportStrategy

class CSVExporter(ExportStrategy):

    def export(self, invoices):
        stream = io.StringIO()
        writer = csv.writer(stream)
        writer.writerow(
            [
                "Filename",
                "Vendor Name",
                "Invoice Number",
                "Invoice Date",
                "GST Number",
                "Total Amount"
            ]
        )

        for invoice in invoices:
            writer.writerows(
                [
                    invoice.filename,
                    invoice.vendor_name,
                    invoice.invoice_number,
                    invoice.invoice_date,
                    invoice.gst_number,
                    invoice.total_amount
                ]
            )

        stream.seek(0)

        return stream