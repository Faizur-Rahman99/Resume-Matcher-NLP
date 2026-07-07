from src.nlp.tokenizer import TextTokenizer


def test_tokenize():

    text = "Python SQL Docker"

    tokens = TextTokenizer.tokenize(text)

    assert tokens == ["Python", "SQL", "Docker"]


def test_tokenize_with_punctuation():

    text = "Python, SQL, Docker."

    tokens = TextTokenizer.tokenize(text)

    assert tokens == ["Python", ",", "SQL", ",", "Docker", "."]