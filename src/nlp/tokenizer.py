from nltk.tokenize import word_tokenize


class TextTokenizer:

    @staticmethod
    def tokenize(text: str) -> list[str]:

        return word_tokenize(text)
