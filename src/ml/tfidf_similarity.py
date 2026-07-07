from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TFIDFSimilarity:

    def calculate(
        self,
        resume_text: str,
        job_text: str
    ) -> float:

        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform(
            [resume_text, job_text]
        )

        score = cosine_similarity(
            vectors[0],
            vectors[1]
        )[0][0]

        return round(float(score), 3)