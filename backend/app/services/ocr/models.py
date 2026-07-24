from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class OCRWord:
    text: str
    confidence: float
    bbox: list[list[int]]


@dataclass(slots=True)
class OCRPage:
    page_number: int
    image_path: Path
    words: list[OCRWord]

@dataclass(slots=True)
class OCRDocument:
    pages: list[OCRPage]