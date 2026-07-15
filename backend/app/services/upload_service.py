from fastapi import UploadFile

from app.models.invoice import Invoice
from app.repositories.invoice_repositiory import InvoiceRepository
from app.utils.file_utils import (
    save_file,
    validate_file,
)

class UploadService:
    def __init__(
        self,
        repository: InvoiceRepository,
    ):
        self.repository = repository

    def upload(
        self,
        upload_file: UploadFile,
    ):
        validate_file(upload_file)

        file_path, _ = save_file(upload_file)

        invoice = Invoice(
            filename=upload_file.filename,
            file_path=str(file_path),
            file_size=file_path.stat().st_size,
            mime_type=upload_file.content_type,
            processing_status="Uploaded",
        )

        return self.repository.create(invoice)
    
    def upload_bulk(
        self,
        files: list[UploadFile],  
    ):
        uploaded = []

        for file in files:
            uploaded.append(
                self.upload(file)
            )

        return uploaded