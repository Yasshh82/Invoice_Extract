from pathlib import Path

try:
    from .dataset.builder import DatasetBuilder
except ImportError:
    from dataset.builder import DatasetBuilder

builder = DatasetBuilder()

dataset_root = Path(__file__).resolve().parent / "dataset" / "sroie" / "train"
builder.build(dataset_root)