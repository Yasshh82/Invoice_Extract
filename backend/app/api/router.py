from fastapi import APIRouter

from app.api.routes import batch, invoices, upload, export

router = APIRouter()

router.include_router(invoices.router)
router.include_router(upload.router)
router.include_router(batch.router)
router.include_router(export.router)