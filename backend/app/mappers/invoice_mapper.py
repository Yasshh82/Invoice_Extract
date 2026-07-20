from app.core.config import settings
from app.schemas.invoice import InvoiceResponse

class InvoiceMapper:

    @staticmethod
    def to_response(invoice):
        return InvoiceResponse(
            id=invoice.id,
            filename=invoice.filename,
            file_url=f"{settings.BACKEND_PUBLIC_URL}/{invoice.file_path}",
            file_size=invoice.file_size,
            mime_type=invoice.mime_tye,
            processing_status=invoice.processing_status,
            uploaded_at=invoice.uploaded_at,
        )
    
    @staticmethod
    def to_response_list(invoices):
        return [InvoiceMapper.to_response(invoice) 
                for invoice in invoices]