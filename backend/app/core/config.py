from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    APP_NAME: str

    DEBUG: bool

    BACKEND_PUBLIC_URL: str

    DATABASE_URL: str

    REDIS_URL: str

    UPLOAD_DIR: str

    MAX_UPLOAD_SIZE_MB: int

    TEMP_DIR: str = "temp"

    PDF_RENDER_DPI: int = 300

    PDF_IMAGE_FORMAT: str = "png"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

settings = Settings()