from dataclasses import dataclass


@dataclass(slots=True)
class InvoiceQuery:
    page: int = 1
    page_size: int = 10
    search: str | None = None
    status: str | None = None
    vendor: str | None = None
    sort_by: str = "uploaded_at"
    descending: bool = True

    @property
    def offset(self):
        return (self.page - 1) * self.page_size