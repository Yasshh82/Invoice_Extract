from pathlib import Path
from datasets import load_from_disk


DATASET_PATH = Path("ml/artifacts/v1/encoded_dataset")

OUTPUT_PATH = Path("ml/artifacts/v1")


def main():

    dataset = load_from_disk(str(DATASET_PATH))

    split = dataset.train_test_split(test_size=0.10, seed=42)

    train_dataset = split["train"]

    validation_dataset = split["test"]

    train_dataset.save_to_disk(str(OUTPUT_PATH / "train_dataset"))

    validation_dataset.save_to_disk(str(OUTPUT_PATH / "validation_dataset"))

    print(
        f"Train: "
        f"{len(train_dataset)}"
    )

    print(
        f"Validation: "
        f"{len(validation_dataset)}"
    )


if __name__ == "__main__":
    main()