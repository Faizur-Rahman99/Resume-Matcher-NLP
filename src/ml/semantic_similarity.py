from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


class SemanticSimilarity:
    """
    Calculates semantic similarity between two texts using a Sentence Transformer.
    """

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def calculate(
        self,
        resume_text: str,
        job_text: str
    ) -> float:
        """
        Compute a semantic similarity score between 0.0 and 1.0.
        """

        embeddings = self.model.encode(
            [resume_text, job_text],
            convert_to_tensor=True
        )

        score = cos_sim(
            embeddings[0],
            embeddings[1]
        ).item()

        return round(float(score), 3)