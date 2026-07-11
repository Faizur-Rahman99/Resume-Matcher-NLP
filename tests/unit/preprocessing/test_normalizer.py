from src.nlp.normalizer import TextNormalizer


def test_lowercase():

    text = "HELLO WORLD"

    assert TextNormalizer.lowercase(text) == "hello world"


def test_remove_punctuation():

    text = "Python, Java!"

    assert TextNormalizer.remove_punctuation(text) == "Python  Java "


def test_remove_extra_spaces():

    text = "Python    Java      SQL"

    assert TextNormalizer.remove_extra_spaces(text) == "Python Java SQL"