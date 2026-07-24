from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class OCRWord:
    text: str
    confidence: float
    bbox: list[list[int]]
    normalized_bbox: list[int]

@dataclass(slots=True)
class OCRPage:
    page_number: int
    image_path: Path
    width: int
    height: int
    words: list[OCRWord]

@dataclass(slots=True)
class OCRDocument:
    pages: list[OCRPage]

    @property
    def words(self):

        words = []
        for page in self.pages:
            words.extend(page.words)

        return words

    @property
    def texts(self):

        return [word.text for word in self.words]