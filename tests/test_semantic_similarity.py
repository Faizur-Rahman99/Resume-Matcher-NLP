from src.ml.semantic_similarity import SemanticSimilarity


def test_semantic_similarity():

    similarity = SemanticSimilarity()

    score = similarity.calculate(
        "Python SQL Docker",
        "Python SQL Docker"
    )

    assert score > 0.95