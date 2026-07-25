from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.router import router
from app.core.config import settings
from app.utils.file_utils import UPLOAD_DIR, ensure_upload_dir
from app.api.exception_handlers import register_exception_handlers

from pathlib import Path

app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(router)

register_exception_handlers(app)

ensure_upload_dir()
Path(settings.TEMP_DIR).mkdir(parents=True, exist_ok=True)

app.mount(
    "/app/uploads",
    StaticFiles(directory=str(UPLOAD_DIR)),
    name="uploads",
)

app.mount(
    "/temp",
    StaticFiles(directory=settings.TEMP_DIR),
    name="temp"
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