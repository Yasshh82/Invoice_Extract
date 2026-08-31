from pathlib import Path

from datasets import load_from_disk


DATASET_PATH = Path("ml/artifacts/v1/train_dataset")


dataset = load_from_disk(str(DATASET_PATH))

print(f"Dataset size: {len(dataset)}")

sample = dataset[0]

print("\nFeatures:")

for key, value in sample.items():
    if hasattr(value, "shape"):
        print(key, value.shape)

    elif isinstance(value, list):
        print(key, len(value))

    else:
        print(key, type(value))