from pathlib import Path

from app.core.config import settings
from app.schemas.invoice import InvoiceResponse

class InvoiceMapper:

    @staticmethod
    def to_response(invoice):
        visualization_dir = Path(settings.TEMP_DIR) / str(invoice.id) / "visualization"
        visualization_urls = []

        if visualization_dir.exists():
            visualization_urls = [
                f"{settings.BACKEND_PUBLIC_URL}/{(Path(settings.TEMP_DIR) / str(invoice.id) / 'visualization' / file_name.name).as_posix().lstrip('/')}"
                for file_name in sorted(visualization_dir.glob("*.png"))
            ]

        return InvoiceResponse(
            id=invoice.id,
            filename=invoice.filename,
            file_url=f"{settings.BACKEND_PUBLIC_URL}/{invoice.file_path}",
            file_size=invoice.file_size,
            mime_type=invoice.mime_tye,
            processing_status=invoice.processing_status,
            visualization_urls=visualization_urls,
            uploaded_at=invoice.uploaded_at,
        )
    
    @staticmethod
    def to_response_list(invoices):
        return [InvoiceMapper.to_response(invoice) 
                for invoice in invoices]