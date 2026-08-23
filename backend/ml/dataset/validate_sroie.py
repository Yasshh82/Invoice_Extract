from pathlib import Path


class SROIEValidator:

    def validate(self, root: Path):

        image_dir = (root / "images")

        labels_dir = (root / "labels")

        ocr_dir = (root / "ocr")

        images = list(image_dir.glob("*"))

        missing_annotations = []

        missing_ocr = []

        for image in images:

            stem = image.stem
            annotation = (labels_dir / f"{stem}.txt")

            ocr = (ocr_dir / f"{stem}.txt")

            if not annotation.exists():
                missing_annotations.append(stem)

            if not ocr.exists():

                missing_ocr.append(stem)

        print(f"Images: {len(images)}")

        print(
            f"Missing annotations: "
            f"{len(missing_annotations)}"
        )

        print(
            f"Missing OCR: "
            f"{len(missing_ocr)}"
        )


if __name__ == "__main__":
    # Define the path to your training data relative to your working directory (ml/)
    target_dir = Path("dataset/sroie/train")
    
    # Create an instance of the validator
    validator = SROIEValidator()
    
    # Run the validation
    print(f"Validating dataset at: {target_dir}")
    validator.validate(target_dir)