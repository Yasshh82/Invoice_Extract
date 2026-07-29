from pathlib import Path

from .loader import SROIEDatasetLoader

from .manifest import DatasetManifest

from .validator import DatasetValidator


class DatasetBuilder:

    def build(self, dataset_root: Path):

        loader = SROIEDatasetLoader(dataset_root)

        documents = loader.load()

        DatasetValidator().validate(documents)

        DatasetManifest().generate(documents, dataset_root / "manifest.json")

        return documents