from nltk.stem import WordNetLemmatizer


class TextLemmatizer:
    """
    Lemmatize a list of tokens.
    """

    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize(self, tokens: list[str]) -> list[str]:
        """
        Lemmatize each token.

        Parameters
        ----------
        tokens : list[str]

        Returns
        -------
        list[str]
        """
        return [
            self.lemmatizer.lemmatize(token)
            for token in tokens
        ]