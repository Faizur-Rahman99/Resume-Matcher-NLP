from src.nlp.ngram_generator import NGramGenerator


def test_unigrams():

    tokens = ["machine", "learning", "python"]

    result = NGramGenerator.generate(tokens, 1)

    assert result == [
        "machine",
        "learning",
        "python"
    ]


def test_bigrams():

    tokens = ["machine", "learning", "python"]

    result = NGramGenerator.generate(tokens, 2)

    assert result == [
        "machine learning",
        "learning python"
    ]


def test_trigrams():

    tokens = ["machine", "learning", "python"]

    result = NGramGenerator.generate(tokens, 3)

    assert result == [
        "machine learning python"
    ]


def test_large_n():

    tokens = ["python", "sql"]

    result = NGramGenerator.generate(tokens, 5)

    assert result == []


def test_invalid_n():

    import pytest

    with pytest.raises(ValueError):
        NGramGenerator.generate(["python"], 0)