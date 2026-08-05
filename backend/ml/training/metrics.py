import evaluate

seqeval = evaluate.load("seqeval")


class Metrics:

    def compute(self, predictions, labels, id_to_label):

        predictions = predictions.argmax(-1)

        true_predictions = []

        true_labels = []

        for prediction, label in zip(predictions, labels):

            pred = []
            truth = []

            for p, l in zip(prediction, label):

                if l == -100:
                    continue

                pred.append(id_to_label[p])

                truth.append(id_to_label[l])

            true_predictions.append(pred)

            true_labels.append(truth)

        results = seqeval.compute(predictions=true_predictions, references=true_labels)

        return {
            "precision": results["overall_precision"],
            "recall": results["overall_recall"],
            "f1": results["overall_f1"],
            "accuracy": results["overall_accuracy"]
        }