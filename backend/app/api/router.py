from fastapi import APIRouter

from app.api.routes import invoices
from app.api.routes import upload

router = APIRouter()

router.include_router(invoices.router)

router.include_router(upload.router)