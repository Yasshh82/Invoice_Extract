from pathlib import Path
import sys

if __package__:
    from .config import TrainingConfig
    from .manager import TrainingManager
    from .model import create_model
    from .trainer import build_training_args
    from ml.prepare_dataset import prepare_dataset
    from ml.preprocessing.processor import LayoutLMProcessor
    from ml.preprocessing.feature_builder import FeatureBuilder
else:
    root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root))

    from config import TrainingConfig
    from manager import TrainingManager
    from model import create_model
    from trainer import build_training_args
    from prepare_dataset import prepare_dataset
    from preprocessing.processor import LayoutLMProcessor
    from preprocessing.feature_builder import FeatureBuilder


def main():
    config = TrainingConfig()

    project_root = Path(__file__).resolve().parents[1]
    train_root = project_root / "dataset" / "sroie" / "train"
    eval_root = project_root / "dataset" / "sroie" / "test"

    encoder = None
    processor = None

    train_dataset_wrapper, _, encoder = prepare_dataset(
        train_root,
        batch_size=config.train_batch_size,
    )

    processor = LayoutLMProcessor(label_encoder=encoder)
    feature_builder = FeatureBuilder()

    eval_dataset_wrapper, _, _ = prepare_dataset(
        eval_root,
        batch_size=config.eval_batch_size,
        processor=processor,
        feature_builder=feature_builder,
        save_artifact=False,
        label_encoder=encoder,
    )

    train_dataset = train_dataset_wrapper.get()
    eval_dataset = eval_dataset_wrapper.get()

    model = create_model(config, config.label_map_path)
    trainer_args = build_training_args(config)

    manager = TrainingManager(
        trainer_args,
        model,
        train_dataset,
        eval_dataset,
        config,
        encoder,
    )

    manager.train()
    metrics = manager.evaluate()
    manager.save_model_bundle(processor)
    manager.save_reports(metrics)


if __name__ == "__main__":
    main()
