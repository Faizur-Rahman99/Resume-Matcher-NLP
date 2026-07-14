from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


class SemanticSimilarity:
    """
    Calculates semantic similarity between two texts using a Sentence Transformer.
    """

    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            cls._model = SentenceTransformer("all-MiniLM-L6-v2")
        return cls._model

    def calculate(
        self,
        resume_text: str,
        job_text: str,
    ) -> float:

        model = self.get_model()

        embeddings = model.encode(
            [resume_text, job_text],
            convert_to_tensor=True,
        )

        score = cos_sim(
            embeddings[0],
            embeddings[1],
        ).item()

        return round(float(score), 3)