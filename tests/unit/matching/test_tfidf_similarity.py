from src.ml.tfidf_similarity import TFIDFSimilarity


def test_identical_documents():

    similarity = TFIDFSimilarity()

    score = similarity.calculate(
        "Python SQL Docker",
        "Python SQL Docker"
    )

    assert score == 1.0


def test_different_documents():

    similarity = TFIDFSimilarity()

    score = similarity.calculate(
        "Python SQL",
        "Java Spring"
    )

    assert score < 0.2


def test_partial_similarity():

    similarity = TFIDFSimilarity()

    score = similarity.calculate(
        "Python SQL Docker",
        "Python SQL AWS"
    )

    assert 0 < score < 1