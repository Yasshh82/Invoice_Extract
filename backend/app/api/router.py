from fastapi import APIRouter
from app.api.routes import invoices

router = APIRouter()

router.include_router(invoices.router)
