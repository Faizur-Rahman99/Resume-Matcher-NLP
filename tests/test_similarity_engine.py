from src.config.scoring import (
    RULE_BASED_WEIGHT,
    TFIDF_WEIGHT,
    SEMANTIC_WEIGHT,
)
from src.entity.job_description import JobDescription
from src.entity.resume import Resume
from src.matching.similarity_engine import SimilarityEngine


def test_similarity_engine():

    resume = Resume(
        skills=["Python", "SQL", "Docker"],
        experience_years=4
    )

    job = JobDescription(
        skills=["Python", "SQL", "Docker", "AWS"],
        experience_years=5
    )

    engine = SimilarityEngine()

    result = engine.match(resume, job)

    assert result.skill_score == 0.75
    assert result.experience_score == 0.8

    assert 0 <= result.rule_based_score <= 1
    assert 0 <= result.tfidf_score <= 1
    assert 0 <= result.semantic_score <= 1
    assert 0 <= result.overall_score <= 1

    expected = round(
        result.rule_based_score * RULE_BASED_WEIGHT
        + result.tfidf_score * TFIDF_WEIGHT
        + result.semantic_score * SEMANTIC_WEIGHT,
        3,
    )

    assert result.overall_score == expected

    assert "AWS" in result.missing_skills