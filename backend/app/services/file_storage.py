from pathlib import Path
import shutil
import uuid

from fastapi import UploadFile

from app.constants.file_constants import ( ALLOWED_EXTENSIONS, ALLOWED_MIME_TYPES, MAX_FILE_SIZE_MB, UPLOAD_DIR)

from app.exceptions.upload_exceptions import (FileSaveException, FileTooLargeException, InvalidFileTypeException, InvalidMimeTypeException)

APP_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = APP_DIR / "uploads"

def ensure_upload_dir():
    """Create uploads directory if it doesn't exist."""
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def validate_file(upload_file: UploadFile):
    """Validate uploaded file extension."""
    extension = Path(upload_file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise InvalidFileTypeException()
    
    if upload_file.content_type not in ALLOWED_MIME_TYPES:
        raise InvalidMimeTypeException()
    
def save_file(upload_file: UploadFile):
    ensure_upload_dir()

    validate_file(upload_file)

    extension = Path(upload_file.filename).suffix.lower()

    unique_filename = f"{uuid.uuid4()}{extension}"

    destination = UPLOAD_DIR / unique_filename

    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)

    except Exception as e:
        raise FileSaveException() from e

    return destination

def delete_file(path:str):
    file = Path(path)

    if file.exists():
        file.unlink()