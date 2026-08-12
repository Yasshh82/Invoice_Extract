from .csv_exporter import CSVExporter
from .json_exporter import JSONExporter

class ExportFactory:
    exporters = {
        "csv": CSVExporter(),
        "json": JSONExporter()
    }

    @classmethod
    def create(cls, fmt):
        exporter = cls.exporters.get(fmt.lower())

        if exporter is None:
            raise ValueError(f"Unsupported export format: {fmt}")

        return exporter