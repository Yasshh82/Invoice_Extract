from datasets import Dataset
from torch.utils.data import DataLoader


class InvoiceDataset:

    def __init__(self, encodings):
        self.dataset = Dataset.from_list(encodings)

    def get(self):
        return self.dataset


class InvoiceDataLoader:

    def __init__(self, dataset, batch_size=2):
        base_dataset = dataset.get() if hasattr(dataset, "get") else dataset
        self.loader = DataLoader(
            base_dataset,
            batch_size=batch_size,
            shuffle=True,
        )

    def get(self):
        return self.loader