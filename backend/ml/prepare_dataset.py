from pathlib import Path
from types import SimpleNamespace

from pathlib import Path
import sys

if __package__:
    from .dataset import InvoiceDataLoader, InvoiceDataset
    from .dataset.builder import DatasetBuilder
    from .preprocessing.feature_builder import FeatureBuilder
    from .preprocessing.processor import LayoutLMProcessor
else:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from ml.dataset import InvoiceDataLoader, InvoiceDataset
    from ml.dataset.builder import DatasetBuilder
    from ml.preprocessing.feature_builder import FeatureBuilder
    from ml.preprocessing.processor import LayoutLMProcessor


class SimpleOCRDocument:
    """Minimal OCR wrapper that exposes page words and normalized boxes."""

    def __init__(self, ocr_path: Path):
        self.path = ocr_path
        self.pages = []

        if not ocr_path.exists():
            return

        words = []
        for line in ocr_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue

            parts = [part.strip() for part in line.split(",")]
            if len(parts) < 9:
                continue

            text = parts[-1]
            bbox = [float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])]
            words.append(SimpleNamespace(text=text, normalized_bbox=bbox))

        if words:
            self.pages.append(SimpleNamespace(words=words))


def prepare_dataset(dataset_root: Path, batch_size: int = 2, processor=None, feature_builder=None):
    builder = DatasetBuilder()
    documents = builder.build(dataset_root)

    processor = processor or LayoutLMProcessor()
    feature_builder = feature_builder or FeatureBuilder()

    encodings = []

    for document in documents:
        ocr_document = SimpleOCRDocument(document.ocr)
        feature = feature_builder.build(document, ocr_document)
        encodings.append(processor.process(feature))

    dataset = InvoiceDataset(encodings)
    loader = InvoiceDataLoader(dataset, batch_size=batch_size)

    return dataset, loader


if __name__ == "__main__":
    dataset_root = Path(__file__).resolve().parent / "dataset" / "sroie" / "train"
    prepare_dataset(dataset_root)