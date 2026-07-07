from nltk.corpus import stopwords


class StopwordRemover:
    """
    Remove unnecessary stopwords while preserving
    important words such as 'no' and 'not'.
    """

    def __init__(self):

        self.stop_words = set(stopwords.words("english"))

        # Preserve negation words
        self.stop_words.discard("no")
        self.stop_words.discard("not")

    def remove(self, tokens: list[str]) -> list[str]:
        """
        Remove stopwords from a list of tokens.
        """

        return [
            token
            for token in tokens
            if token.lower() not in self.stop_words
        ]