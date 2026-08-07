from typing import List

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
)

from app.api.dependencies import (
    get_upload_service,
)

from app.schemas.upload import (
    BulkUploadResponse,
    UploadResponse,
)

from app.services.upload_service import (
    UploadService,
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/", response_model=UploadResponse)
async def upload_file(
    file: UploadFile = File(...),
    service: UploadService = Depends(get_upload_service),
):
    return service.upload(file)


@router.post("/bulk", response_model=BulkUploadResponse)
async def upload_bulk(
    files: List[UploadFile] = File(...),
    service: UploadService = Depends(get_upload_service),
):
    return service.upload_bulk(files)