from pathlib import Path

from transformers import LayoutLMv3Processor

from .artifact import load_training_artifact
from .label_map import load_label_map


class LayoutLMProcessor:

    def __init__(self, label_map_path: str | Path | None = None, label_encoder=None):

        self.processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)

        if label_encoder is not None:
            self.label_to_id = label_encoder.label_to_id
        else:
            label_map_path = Path(label_map_path or Path(__file__).resolve().parents[1] / "artifacts" / "v1" / "label_map.json")

            if label_map_path.exists():
                self.label_to_id = load_label_map(label_map_path).label_to_id
            else:
                artifact = load_training_artifact(Path(__file__).resolve().parents[1] / "artifacts" / "v1")
                self.label_to_id = artifact["encoder"].label_to_id

    def process(self, feature):

        encoding = self.processor(
            images=feature.image,
            text=feature.words,
            boxes=feature.boxes,
            word_labels=[self.label_to_id[x] for x in feature.labels],
            truncation=True,
            padding="max_length",
            return_tensors="pt",
        )

        return encoding