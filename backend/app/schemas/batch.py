from datetime import datetime

from pydantic import BaseModel

class BatchResponse(BaseModel):
    id: str
    status: str
    total: int
    completed: int
    failed: int
    percentage: float
    created_at: datetime
    finished_at: datetime | None
