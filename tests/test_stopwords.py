from src.nlp.stopwords import StopwordRemover


def test_remove_stopwords():

    remover = StopwordRemover()

    tokens = [
        "I",
        "have",
        "experience",
        "with",
        "Python"
    ]

    cleaned = remover.remove(tokens)

    assert cleaned == ["experience", "Python"]


def test_preserve_no_and_not():

    remover = StopwordRemover()

    tokens = [
        "not",
        "experienced",
        "with",
        "Docker"
    ]

    cleaned = remover.remove(tokens)

    assert cleaned == [
        "not",
        "experienced",
        "Docker"
    ]