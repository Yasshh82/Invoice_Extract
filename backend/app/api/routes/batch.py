from fastapi import APIRouter

from app.batch.manager import tracker

router = APIRouter(
    prefix="/batch",
    tags=["Batch"],
)


@router.get("/{batch_id}")
def get_status(batch_id: str):
    return tracker.get(batch_id)
