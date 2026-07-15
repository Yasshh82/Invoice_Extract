from pathlib import Path
import shutil
import uuid

from fastapi import UploadFile

APP_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = APP_DIR / "uploads"

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png"
}

def ensure_upload_dir():
    """Create uploads directory if it doesn't exist."""
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def validate_file(upload_file: UploadFile):
    """Validate uploaded file extension."""
    extension = Path(upload_file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {extension}. Allowed types are: {', '.join(ALLOWED_EXTENSIONS)}")
    
def save_file(upload_file: UploadFile):
    ensure_upload_dir()

    extension = Path(upload_file.filename).suffix.lower()

    unique_filename = f"{uuid.uuid4()}{extension}"

    destination = UPLOAD_DIR / unique_filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return destination, unique_filename