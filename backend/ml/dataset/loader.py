from pathlib import Path

from .models import TrainingDocument
from .parser import SROIEParser


class SROIEDatasetLoader:

    def __init__(self, dataset_root: Path):
        self.root = dataset_root
        self.parser = SROIEParser()

    def _resolve_ocr_path(self, stem: str, ocr_dir: Path) -> Path:
        for suffix in (".json", ".txt"):
            candidate = ocr_dir / f"{stem}{suffix}"
            if candidate.exists():
                return candidate

        raise FileNotFoundError(
            f"No OCR file found for {stem} in {ocr_dir} (tried .json and .txt)"
        )

    def load(self):
        documents = []

        image_dir = self.root / "images"
        ocr_dir = self.root / "ocr"
        label_dir = self.root / "labels"

        for image in image_dir.glob("*"):
            stem = image.stem
            label_path = label_dir / f"{stem}.txt"
            ocr_path = self._resolve_ocr_path(stem, ocr_dir)

            document = TrainingDocument(
                image=image,
                ocr=ocr_path,
                label=label_path,
                entities=self.parser.parse(label_path)
            )

            documents.append(document)

        return documents