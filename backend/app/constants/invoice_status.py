from enum import StrEnum

class InvoiceStatus(StrEnum):
    UPLOADED = "Uploaded"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    FAILED = "Failed"