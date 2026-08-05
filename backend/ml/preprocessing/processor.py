from pathlib import Path

from transformers import LayoutLMv3Processor

from .artifact import load_training_artifact, get_model_dir
from .label_map import load_label_map


class LayoutLMProcessor:

    def __init__(
        self,
        model_dir: str | Path | None = None,
        label_map_path: str | Path | None = None,
        label_encoder=None,
    ):
        artifact_root = Path(__file__).resolve().parents[1] / "artifacts" / "v1"
        if model_dir is None:
            model_dir = get_model_dir(artifact_root)
        else:
            model_dir = Path(model_dir)

        if model_dir.exists():
            try:
                self.processor = LayoutLMv3Processor.from_pretrained(model_dir, apply_ocr=False)
            except Exception:
                self.processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
        else:
            self.processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)

        if label_encoder is not None:
            self.encoder = label_encoder
            self.label_to_id = self.encoder.label_to_id
        else:
            if label_map_path is not None:
                label_map_path = Path(label_map_path)
            else:
                candidate = model_dir / "label_map.json"
                if candidate.exists():
                    label_map_path = candidate
                else:
                    fallback = artifact_root / "model" / "label_map.json"
                    label_map_path = fallback if fallback.exists() else artifact_root / "label_map.json"

            if not label_map_path.exists():
                artifact = load_training_artifact(artifact_root)
                self.encoder = artifact["encoder"]
            else:
                self.encoder = load_label_map(label_map_path)

            self.label_to_id = self.encoder.label_to_id

    def save_pretrained(self, save_directory: str | Path):
        save_directory = Path(save_directory)
        save_directory.mkdir(parents=True, exist_ok=True)
        self.processor.save_pretrained(save_directory)

        if hasattr(self, "encoder"):
            output_path = save_directory / "label_map.json"
            self.encoder.save(output_path)

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