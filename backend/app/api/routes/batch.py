from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_batch_service
from app.schemas.batch import BatchResponse
from app.services.batch_service import BatchService

router = APIRouter(
    prefix="/batch",
    tags=["Batch"],
)


@router.get("/{batch_id}", response_model=BatchResponse,)
def get_batch(
    batch_id: str,
    service: BatchService = Depends(get_batch_service),
):
    batch = service.get(batch_id)
    if batch is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Batch not found",
        )
    return batch
