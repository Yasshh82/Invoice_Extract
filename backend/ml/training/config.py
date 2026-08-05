from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class TrainingConfig:

    model_name: str = "microsoft/layoutlmv3-base"
    artifact_dir: str = "ml/artifacts/v1"
    checkpoint_dir: str = "ml/artifacts/v1/checkpoints"
    num_epochs: int = 10
    train_batch_size: int = 2
    eval_batch_size: int = 2
    learning_rate: float = 2e-5
    weight_decay: float = 0.01
    warmup_ratio: float = 0.1
    max_length: int = 512
    seed: int = 42

    @property
    def model_dir(self) -> str:
        return str(Path(self.artifact_dir) / "model")

    @property
    def reports_dir(self) -> str:
        return str(Path(self.artifact_dir) / "reports")

    @property
    def label_map_path(self) -> str:
        return str(Path(self.model_dir) / "label_map.json")