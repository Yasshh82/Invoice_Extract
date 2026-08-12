from .factory import ExportFactory

class ExportService:
    def export(self, invoices, fmt):
        exporter = ExportFactory.create(fmt)
        return exporter.export(invoices)