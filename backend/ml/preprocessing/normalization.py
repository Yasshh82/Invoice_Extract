import re
import string


class TextNormalizer:

    def __init__(self, remove_punctuation: bool = False):
        self.remove_punctuation = remove_punctuation

    def normalize(self, text: str) -> str:
        text = text.lower()

        if self.remove_punctuation:
            text = text.translate(str.maketrans("", "", string.punctuation))

        text = re.sub(r"\s+", " ", text)

        return text.strip()