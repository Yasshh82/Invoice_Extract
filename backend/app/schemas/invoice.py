from datetime import date, datetime
from pydantic import BaseModel, ConfigDict

class InvoiceBase(BaseModel):
    
    filename: str
    vendor_name: str | None = None
    invoice_number: str | None = None
    invoice_date: date | None = None
    gst_number: str | None = None
    total_amount: float | None = None

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceResponse(BaseModel):

    id: int
    filename: str
    file_url: str
    file_size: int
    mime_type: str
    processing_status: str
    uploaded_at: datetime
    model_config = ConfigDict(from_attributes=True)