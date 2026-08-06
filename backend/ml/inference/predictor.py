import torch


class Predictor:

    def __init__(self, model):

        self.model = model
        self.model.eval()


    @torch.no_grad()
    def predict(self, encoding):
        output = self.model(**encoding)

        predictions = (output.logits.argmax(-1).squeeze().tolist())

        confidence = (torch.softmax(output.logits, dim=-1).max(-1).values.squeeze().tolist())

        return (predictions, confidence)