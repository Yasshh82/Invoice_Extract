from pathlib import Path


def prepare_checkpoint_dir(output_dir: str):

    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)

    return path