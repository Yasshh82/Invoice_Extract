import json

from datetime import datetime


class TrainingReport:

    @staticmethod
    def save(config, metrics, output):

        report = {
            "created_at": datetime.utcnow().isoformat(),
            "model": config.model_name,
            "epochs": config.num_epochs,
            "learning_rate": config.learning_rate,
            "metrics": metrics,
        }

        with open(output, "w", encoding="utf8") as file:
            json.dump(report, file, indent=4)