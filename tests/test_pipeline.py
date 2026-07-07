from src.nlp.pipeline import NLPPipeline


def test_pipeline():

    pipeline = NLPPipeline()

    tokens = pipeline.process(
        "Experienced in Python, SQL Server and Docker."
    )

    assert "python" in [token.lower() for token in tokens]
    assert "docker" in [token.lower() for token in tokens]