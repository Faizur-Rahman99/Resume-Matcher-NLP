from fastapi import APIRouter, HTTPException

from src.api.schemas import (
    BatchMatchRequest,
    BatchMatchResponse,
    CandidateResult,
    MatchRequest,
    MatchResponse,
)
from src.entity.job_description import JobDescription
from src.entity.resume import Resume
from src.matching.similarity_engine import SimilarityEngine

router = APIRouter(
    tags=["Matching"]
)

engine = SimilarityEngine()


def build_resume(resume_data) -> Resume:
    return Resume(
        skills=resume_data.skills,
        experience_years=resume_data.experience_years,
    )


def build_job(job_data) -> JobDescription:
    return JobDescription(
        skills=job_data.skills,
        experience_years=job_data.experience_years,
    )


@router.post(
    "/match",
    summary="Match one resume against one job",
    response_model=MatchResponse,
)
def match(
    request: MatchRequest,
) -> MatchResponse:

    try:

        resume = build_resume(
            request.resume
        )

        job = build_job(
            request.job
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
            matched_skills=result.matched_skills,
            missing_skills=result.missing_skills,
            explanation=result.explanation,
        )

    except Exception as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@router.post(
    "/match/batch",
    summary="Rank multiple resumes against one job",
    response_model=BatchMatchResponse,
)
def batch_match(
    request: BatchMatchRequest,
) -> BatchMatchResponse:

    try:

        job = build_job(
            request.job
        )

        results = []

        for resume_data in request.resumes:

            resume = build_resume(
                resume_data
            )

            match = engine.match(
                resume,
                job,
            )

            results.append(
                CandidateResult(
                    filename=resume_data.filename,
                    name=resume_data.name,
                    email=resume_data.email,
                    phone=resume_data.phone,
                    education=resume_data.education,
                    projects=resume_data.projects,
                    overall_score=match.overall_score,
                    skill_score=match.skill_score,
                    experience_score=match.experience_score,
                    matched_skills=match.matched_skills,
                    missing_skills=match.missing_skills,
                    explanation=match.explanation,
                )
            )

        results.sort(
            key=lambda candidate: candidate.overall_score,
            reverse=True,
        )

        return BatchMatchResponse(
            results=results
        )

    except Exception as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )