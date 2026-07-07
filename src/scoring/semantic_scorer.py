from src.ml.semantic_similarity import SemanticSimilarity


class SemanticScorer:

    def __init__(self):
        self.model = SemanticSimilarity()

    def calculate(
        self,
        resume_text: str,
        job_text: str,
    ) -> float:

        return self.model.calculate(
            resume_text,
            job_text,
        )