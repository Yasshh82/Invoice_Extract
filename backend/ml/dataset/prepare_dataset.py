import json
from pathlib import Path

from transformers import LayoutLMv3Processor
from .sroie_loader import SROIEDatasetLoader
from .alignment import EntityAligner
from .bio import create_bio_labels
from .label_encoder import LabelEncoder
from .layoutlm_dataset import LayoutLMDatasetBuilder
from .alignment_report import print_alignment_report


TRAIN_ROOT = Path("ml/dataset/sroie/train")
ARTIFACT_ROOT = Path("ml/artifacts/v1")


def prepare_documents():
    loader = SROIEDatasetLoader(TRAIN_ROOT)

    documents = loader.load()

    aligner = EntityAligner(threshold=75)

    diagnostics = []

    for document in documents:

        words, alignments = aligner.align(document["words"], document["entities"])

        labels = create_bio_labels(len(words), alignments)

        document["words"] = words

        document["bio_labels"] = labels

        diagnostics.extend(alignments)

    return documents, diagnostics


def save_diagnostics(diagnostics):
    output = []

    for item in diagnostics:
        output.append({
            "entity": item.entity_label,
            "value": item.entity_value,
            "start": item.start,
            "end": item.end,
            "score": item.score,
            "status": item.status,
        })

    path = (ARTIFACT_ROOT / "alignment_diagnostics.json")

    with open(path, "w", encoding="utf-8") as file:
        json.dump(output, file, indent=4)


def main():
    documents, diagnostics = prepare_documents()

    encoder = LabelEncoder()
    encoder.fit(documents)
    encoder.save(ARTIFACT_ROOT / "label_map.json")

    processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)   

    builder = LayoutLMDatasetBuilder(processor, encoder)

    dataset = builder.build(documents)

    print_alignment_report(diagnostics)

    dataset.save_to_disk(str(ARTIFACT_ROOT / "train_dataset"))

    save_diagnostics(diagnostics)

    print(f"Documents: {len(dataset)}")
    print(f"Labels: {len(encoder.label_to_id)}")
    print("Dataset saved.")


if __name__ == "__main__":
    main()