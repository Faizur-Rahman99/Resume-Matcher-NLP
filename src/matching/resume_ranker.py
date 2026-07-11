from src.entity.candidate import Candidate
from src.entity.job_description import JobDescription
from src.entity.resume import Resume
from src.matching.similarity_engine import SimilarityEngine


class ResumeRanker:
    """
    Ranks resumes against a job description using the similarity engine.
    """

    def __init__(self):
        self.engine = SimilarityEngine()

    def rank(
        self,
        resumes: list[Resume],
        job: JobDescription
    ) -> list[Candidate]:
        """
        Score and rank resumes from best to worst match.
        """

        candidates = []

        for resume in resumes:

            result = self.engine.match(resume, job)

            candidates.append(
                Candidate(
                    resume=resume,
                    match_result=result
                )
            )

        candidates.sort(
            key=lambda candidate: candidate.match_result.overall_score,
            reverse=True
        )

        return candidates