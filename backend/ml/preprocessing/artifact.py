import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .label_encoder import LabelEncoder


DEFAULT_ARTIFACT_VERSION = "v1"
DEFAULT_MODEL_NAME = "microsoft/layoutlmv3-base"
DEFAULT_MAX_LENGTH = 512
DEFAULT_IMAGE_SIZE = 224
DEFAULT_DATASET_NAME = "SROIE"
DEFAULT_DATASET_VERSION = "SROIE-v1"


def get_default_artifact_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "artifacts" / DEFAULT_ARTIFACT_VERSION


def save_training_artifact(
    encoder: LabelEncoder,
    artifact_dir: str | Path | None = None,
    *,
    model_name: str = DEFAULT_MODEL_NAME,
    max_length: int = DEFAULT_MAX_LENGTH,
    image_size: int = DEFAULT_IMAGE_SIZE,
    dataset_name: str = DEFAULT_DATASET_NAME,
    num_documents: int | None = None,
    dataset_version: str = DEFAULT_DATASET_VERSION,
    created_at: str | None = None,
) -> Path:
    artifact_dir = Path(artifact_dir or get_default_artifact_dir())
    artifact_dir.mkdir(parents=True, exist_ok=True)

    label_map_path = artifact_dir / "label_map.json"
    encoder.save(label_map_path)

    config = {
        "model_name": model_name,
        "max_length": max_length,
        "image_size": image_size,
        "dataset": dataset_name,
        "label_map": label_map_path.name,
    }

    metadata = {
        "created_at": created_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "num_documents": num_documents if num_documents is not None else 0,
        "num_labels": len(encoder.label_to_id),
        "dataset_version": dataset_version,
    }

    config_path = artifact_dir / "config.json"
    metadata_path = artifact_dir / "metadata.json"

    with config_path.open("w", encoding="utf8") as file:
        json.dump(config, file, indent=4)

    with metadata_path.open("w", encoding="utf8") as file:
        json.dump(metadata, file, indent=4)

    return artifact_dir


def load_training_artifact(artifact_dir: str | Path) -> dict[str, Any]:
    artifact_dir = Path(artifact_dir)

    config_path = artifact_dir / "config.json"
    metadata_path = artifact_dir / "metadata.json"
    label_map_path = artifact_dir / "label_map.json"

    if not config_path.exists() or not metadata_path.exists() or not label_map_path.exists():
        raise FileNotFoundError(f"Training artifact is incomplete: {artifact_dir}")

    with config_path.open(encoding="utf8") as file:
        config = json.load(file)

    with metadata_path.open(encoding="utf8") as file:
        metadata = json.load(file)

    encoder = LabelEncoder.load(label_map_path)

    return {"artifact_dir": artifact_dir, "config": config, "metadata": metadata, "encoder": encoder}
