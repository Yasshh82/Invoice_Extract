from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.repositories.invoice_repositiory import InvoiceRepository
from app.services.invoice_service import InvoiceService

def get_invoice_service(
        db: Session = Depends(get_db)
):
    repository = InvoiceRepository(db)
    return InvoiceService(repository)