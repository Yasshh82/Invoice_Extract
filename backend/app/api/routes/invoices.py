from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import get_invoice_service
from app.schemas.invoice import InvoiceCreate, InvoiceResponse
from app.services.invoice_service import InvoiceService

router = APIRouter(prefix="/invoices", tags=["Invoices"])

@router.post("/", response_model=InvoiceResponse)
def create_invoice(
    invoice: InvoiceCreate,
    service: InvoiceService = Depends(get_invoice_service)
):
    return service.create_invoice(invoice)

@router.get("/", response_model=list[InvoiceResponse])
def get_all(
    service: InvoiceService = Depends(get_invoice_service)
):
    return service.get_all()

@router.get("/{invoice_id}", response_model=InvoiceResponse)
def get_invoice(
    invoice_id: int,
    service: InvoiceService = Depends(get_invoice_service)
):
    invoice = service.get(invoice_id)

    if invoice is None:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found"
        )
    
    return invoice

@router.delete("/{invoice_id}")
def delete_invoice(
    invoice_id: int,
    service: InvoiceService = Depends(get_invoice_service)
):
    invoice = service.get(invoice_id)

    if invoice is None:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found"
        )
    
    service.delete(invoice)

    return {"message": "Invoice deleted"}
