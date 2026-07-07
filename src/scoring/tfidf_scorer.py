from src.ml.tfidf_similarity import TFIDFSimilarity


class TFIDFScorer:

    def __init__(self):
        self.model = TFIDFSimilarity()

    def calculate(
        self,
        resume_text: str,
        job_text: str,
    ) -> float:

        return self.model.calculate(
            resume_text,
            job_text,
        )