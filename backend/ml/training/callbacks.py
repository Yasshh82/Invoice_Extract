from transformers import EarlyStoppingCallback


def get_callbacks():

    return [EarlyStoppingCallback(early_stopping_patience=3)]