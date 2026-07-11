from src.nlp.lemmatizer import TextLemmatizer


def test_lemmatizer():

    lemmatizer = TextLemmatizer()

    tokens = [
        "developed",
        "developing",
        "developers",
        "cars"
    ]

    result = lemmatizer.lemmatize(tokens)

    assert result == [
        "developed",
        "developing",
        "developer",
        "car"
    ]