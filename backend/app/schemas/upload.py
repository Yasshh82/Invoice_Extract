from datetime import datetime
from pydantic import BaseModel, ConfigDict

class UploadResponse(BaseModel):
    
    id: int
    filename: str
    file_path: str
    file_size: int
    mime_type: str
    processing_status: str
    uploaded_at: datetime
    
    model_config = ConfigDict(
        from_attributes=True
    )