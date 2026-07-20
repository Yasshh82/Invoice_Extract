from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.router import router
from app.core.config import settings
from app.utils.file_utils import UPLOAD_DIR, ensure_upload_dir
from app.api.exception_handlers import register_exception_handlers

app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(router)

register_exception_handlers(app)

ensure_upload_dir()

app.mount(
    "/app/uploads",
    StaticFiles(directory=str(UPLOAD_DIR)),
    name="uploads",
)

@app.get("/")
def root():
    return {
        "message": "Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }