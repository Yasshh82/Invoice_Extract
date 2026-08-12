from pydantic import BaseModel


class PaginatedInvoices(BaseModel):
    total: int
    page: int
    page_size: int
    items: list