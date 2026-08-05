import json


class TrainingHistory:

    @staticmethod
    def save(trainer, output):

        history = (trainer.state.log_history)

        with open(output, "w", encoding="utf8") as file:
            json.dump(history, file, indent=4)