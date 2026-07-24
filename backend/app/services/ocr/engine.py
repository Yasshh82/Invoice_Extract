from pathlib import Path

from .models import OCRDocument


class OCREngine:

    def __init__(self, backend):
        self.backend = backend


    def process(self, images: list[Path]):

        pages = []

        for index, image in enumerate(images):
            pages.append(self.backend.recognize(image, index + 1))

        return OCRDocument(pages=pages)