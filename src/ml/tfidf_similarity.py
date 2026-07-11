from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TFIDFSimilarity:
    """
    Calculates cosine similarity between two texts using TF-IDF vectors.
    """

    def calculate(
        self,
        resume_text: str,
        job_text: str,
    ) -> float:
        """
        Compute a TF-IDF cosine similarity score between 0.0 and 1.0.
        """

        vectorizer = TfidfVectorizer()

        tfidf_vectors = vectorizer.fit_transform(
            [resume_text, job_text]
        )

        score = cosine_similarity(
            tfidf_vectors[0],
            tfidf_vectors[1],
        )[0][0]

        return round(float(score), 3)