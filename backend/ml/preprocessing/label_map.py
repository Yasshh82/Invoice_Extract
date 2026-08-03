from pathlib import Path

from .label_encoder import LabelEncoder


def load_label_map(path: str | Path) -> LabelEncoder:
    return LabelEncoder.load(path)


def save_label_map(encoder: LabelEncoder, path: str | Path) -> Path:
    output_path = Path(path)
    encoder.save(output_path)
    return output_path
