from pathlib import Path

from transformers import Trainer
from transformers import TrainingArguments


def build_training_args(config):
    checkpoint_dir = Path(config.checkpoint_dir)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    return TrainingArguments(
        output_dir=str(checkpoint_dir),
        learning_rate=config.learning_rate,
        per_device_train_batch_size=config.train_batch_size,
        per_device_eval_batch_size=config.eval_batch_size,
        num_train_epochs=config.num_epochs,
        weight_decay=config.weight_decay,
        warmup_ratio=config.warmup_ratio,
        save_strategy="epoch",
        evaluation_strategy="epoch",
        logging_strategy="steps",
        logging_steps=50,
        seed=config.seed,
        report_to="none",
        load_best_model_at_end=True,
        metric_for_best_model="f1",
        greater_is_better=True,
        save_total_limit=2,
    )


class InvoiceTrainer:

    def __init__(self, model, train_dataset, eval_dataset, config):

        args = build_training_args(config)

        self.trainer = Trainer(
            model=model,
            args=args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
        )