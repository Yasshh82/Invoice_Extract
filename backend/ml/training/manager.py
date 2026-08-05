from pathlib import Path

from transformers import Trainer

from .callbacks import get_callbacks
from .metrics import Metrics
from .history import TrainingHistory
from .report import TrainingReport


class TrainingManager:

    def __init__(self, trainer_args, model, train_dataset, eval_dataset, config, encoder):

        metrics = Metrics()
        self.config = config
        self.encoder = encoder
        self.trainer = Trainer(
            model=model,
            args=trainer_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            callbacks=get_callbacks(),
            compute_metrics=lambda x:
                metrics.compute(
                    x.predictions,
                    x.label_ids,
                    encoder.id_to_label
                )
        )

    def train(self):
        return self.trainer.train()

    def evaluate(self):
        return self.trainer.evaluate()

    def save_model_bundle(self, processor=None):
        model_dir = Path(self.config.model_dir)
        model_dir.mkdir(parents=True, exist_ok=True)

        self.trainer.model.save_pretrained(model_dir, variant="safetensors")

        if processor is None:
            from ml.preprocessing.processor import LayoutLMProcessor
            processor = LayoutLMProcessor(label_encoder=self.encoder)

        processor.save_pretrained(model_dir)

        if self.encoder is not None:
            self.encoder.save(model_dir / "label_map.json")

    def save_reports(self, metrics):
        output = Path(self.config.reports_dir)
        output.mkdir(parents=True, exist_ok=True)

        TrainingHistory.save(self.trainer, output / "history.json")
        TrainingReport.save(self.config, metrics, output / "report.json")