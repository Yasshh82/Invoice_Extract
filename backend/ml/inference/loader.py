from pathlib import Path

from transformers import LayoutLMv3ForTokenClassification, LayoutLMv3Processor

from ml.preprocessing.label_encoder import LabelEncoder


class ModelLoader:

    def __init__(self, model_dir: Path):

        self.processor = (LayoutLMv3Processor.from_pretrained(model_dir))

        self.model = (LayoutLMv3ForTokenClassification.from_pretrained(model_dir))

        self.encoder = (LabelEncoder.load(model_dir / "label_map.json"))