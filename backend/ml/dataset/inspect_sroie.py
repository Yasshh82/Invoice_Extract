from pathlib import Path

from .sroie_loader import SROIEDatasetLoader


ROOT = Path("dataset/sroie/train")


loader = SROIEDatasetLoader(ROOT)

documents = loader.load()

print(f"Documents: {len(documents)}")

if documents:
    document = documents[0]

    print("\nImage:")
    print(document["image"])
    print("\nEntities:")

    for entity in document["entities"]:
        print(entity)

    print("\nOCR words:")

    for word in document["words"][:10]:
        print(word)