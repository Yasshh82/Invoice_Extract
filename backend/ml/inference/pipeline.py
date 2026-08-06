from pathlib import Path

from ml.postprocessing.pipeline import PostProcessingPipeline

from .aggregator import EntityAggregator
from .decoder import PredictionDecoder
from .loader import ModelLoader
from .predictor import Predictor


class InferencePipeline:

    def __init__(self, model_dir: Path):

        loader = ModelLoader(model_dir)
        self.processor = loader.processor
        self.encoder = loader.encoder
        self.predictor = Predictor(loader.model)
        self.decoder = PredictionDecoder()
        self.aggregator = EntityAggregator()
        

    def run(self, feature_document):

        encoding = self.processor(
            images=feature_document.image,
            text=feature_document.words,
            boxes=feature_document.boxes,
            truncation=True,
            return_tensors="pt"
        )

        predictions, confidence = (self.predictor.predict(encoding))

        entities = self.decoder.decode(
            feature_document.words,
            predictions,
            confidence,
            self.encoder,
            feature_document.boxes,
            feature_document.page_numbers,
        )

        structured = self.aggregator.aggregate(entities)
        pipeline = PostProcessingPipeline()

        return pipeline.process(structured)