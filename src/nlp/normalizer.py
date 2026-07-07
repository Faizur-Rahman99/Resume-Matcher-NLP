import re


class TextNormalizer:
    

    @staticmethod
    def lowercase(text: str) -> str:

        return text.lower()

    @staticmethod
    def remove_punctuation(text: str) -> str:

        return re.sub(r"[^\w\s]", " ", text)

    @staticmethod
    def remove_extra_spaces(text: str) -> str:

        return re.sub(r"\s+", " ", text).strip()

    @staticmethod
    def normalize(text: str) -> str:
        text = TextNormalizer.lowercase(text)
        text = TextNormalizer.remove_punctuation(text)
        text = TextNormalizer.remove_extra_spaces(text)

        return text