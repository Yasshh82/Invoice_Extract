from typing import List

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException,
)

from app.api.dependencies import (
    get_upload_service,
)

from app.schemas.upload import (
    UploadResponse,
)

from app.services.upload_service import (
    UploadService,
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

@router.post("/", response_model=UploadResponse,)
async def upload_file(
    file: UploadFile = File(...),
    service: UploadService = Depends(get_upload_service),
):
    return service.upload(file)

        
@router.post("/bulk", response_model=list[UploadResponse])
async def upload_bulk(
    files: List[UploadFile] = File(...),
    service: UploadService = Depends(get_upload_service),
):
    uploaded = []
    for file in files:
        uploaded.append(service.upload(file))
    return uploaded