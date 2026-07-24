from abc import ABC
from abc import abstractmethod

from pathlib import Path
from .models import OCRPage


class OCRBackend(ABC):

    @abstractmethod
    def recognize(self, image: Path, page_number: int) -> OCRPage:
        ...