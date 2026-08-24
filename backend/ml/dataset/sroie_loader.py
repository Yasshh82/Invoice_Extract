from pathlib import Path

from .sroie_builder import SROIEDocumentBuilder


class SROIEDatasetLoader:

    def __init__(self, root: Path):
        self.root = root
        self.image_dir = (root / "images")
        self.ocr_dir = (root / "ocr")
        self.label_dir = (root / "labels")
        self.builder = SROIEDocumentBuilder()
        

    def load(self):

        documents = []

        for image_path in sorted(self.image_dir.glob("*")):

            stem = image_path.stem

            ocr_path = (self.ocr_dir / f"{stem}.txt")

            label_path = (self.label_dir / f"{stem}.txt")

            if not ocr_path.exists():
                continue

            if not label_path.exists():
                continue

            document = self.builder.build(image_path, ocr_path, label_path)

            documents.append(document)

        return documents