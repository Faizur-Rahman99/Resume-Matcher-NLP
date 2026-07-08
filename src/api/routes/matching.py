from fastapi import APIRouter

from src.api.schemas import MatchRequest, MatchResponse
from src.entity.job_description import JobDescription
from src.entity.resume import Resume
from src.matching.similarity_engine import SimilarityEngine


router = APIRouter()

engine = SimilarityEngine()


@router.post(
    "/match",
    response_model=MatchResponse,
)
def match(request: MatchRequest):

    resume = Resume(
        skills=request.resume.skills,
        experience_years=request.resume.experience_years,
    )

    job = JobDescription(
        skills=request.job.skills,
        experience_years=request.job.experience_years,
    )

    result = engine.match(
        resume,
        job,
    )

    return MatchResponse(
        overall_score=result.overall_score,
        rule_based_score=result.rule_based_score,
        tfidf_score=result.tfidf_score,
        semantic_score=result.semantic_score,
        skill_score=result.skill_score,
        experience_score=result.experience_score,
        missing_skills=result.missing_skills,
    )