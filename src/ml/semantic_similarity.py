from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


class SemanticSimilarity:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def calculate(
        self,
        resume_text: str,
        job_text: str
    ) -> float:

        embeddings = self.model.encode(
            [resume_text, job_text],
            convert_to_tensor=True
        )

        score = cos_sim(
            embeddings[0],
            embeddings[1]
        ).item()

        return round(score, 3)