from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import get_invoice_service
from app.schemas.invoice import InvoiceCreate, InvoiceResponse, InvoiceStatusResponse
from app.services.invoice_service import InvoiceService

router = APIRouter(prefix="/invoices", tags=["Invoices"])

@router.post("/", response_model=InvoiceResponse)
def create_invoice(invoice: InvoiceCreate, service: InvoiceService = Depends(get_invoice_service)):
    
    return service.create_invoice(invoice)

@router.get("/", response_model=list[InvoiceResponse])
def get_invoices(service: InvoiceService = Depends(get_invoice_service)):

    return service.get_all()

@router.get("/{invoice_id}", response_model=InvoiceResponse)
def get_invoice(invoice_id: int, service: InvoiceService = Depends(get_invoice_service)):

    invoice = service.get(invoice_id)
    
    return invoice

@router.get("/{invoice_id}/status", response_model=InvoiceStatusResponse)
def get_invoice_status(invoice_id: int, service: InvoiceService = Depends(get_invoice_service)):
    return service.get_status(invoice_id)

@router.delete("/{invoice_id}", status_code=204)
def delete_invoice(invoice_id: int, service: InvoiceService = Depends(get_invoice_service)):

    service.delete(invoice_id)
