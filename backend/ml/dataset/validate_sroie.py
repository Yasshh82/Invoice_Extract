from pathlib import Path


def validate_dataset(root: Path):
    image_dir = root / "images"
    ocr_dir = root / "ocr"
    label_dir = root / "labels"

    images = list(image_dir.glob("*"))

    missing_ocr = []
    missing_labels = []

    for image in images:
        stem = image.stem

        if not (ocr_dir / f"{stem}.txt").exists():
            missing_ocr.append(stem)

        if not (label_dir / f"{stem}.txt").exists():
            missing_labels.append(stem)

    print(f"Images: {len(images)}")

    print(
        f"Missing OCR: "
        f"{len(missing_ocr)}"
    )

    print(
        f"Missing labels: "
        f"{len(missing_labels)}"
    )

    if missing_ocr:
        print("First missing OCR:")
        print(missing_ocr[:10])

    if missing_labels:
        print("First missing labels:")
        print(missing_labels[:10])