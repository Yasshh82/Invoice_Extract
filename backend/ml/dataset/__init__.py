from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_dataset_module_path = Path(__file__).resolve().parent.parent / "dataset.py"
_dataset_spec = spec_from_file_location("ml_dataset_module", _dataset_module_path)
_dataset_module = module_from_spec(_dataset_spec)
_dataset_spec.loader.exec_module(_dataset_module)

InvoiceDataset = _dataset_module.InvoiceDataset
InvoiceDataLoader = _dataset_module.InvoiceDataLoader
