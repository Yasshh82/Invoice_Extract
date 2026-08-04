from transformers import Trainer
from transformers import TrainingArguments


class InvoiceTrainer:

    def __init__(self, model, train_dataset, eval_dataset, config):

        args = TrainingArguments(
            output_dir=config.output_dir,
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
        )

        self.trainer = Trainer(
            model=model,
            args=args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset
        )