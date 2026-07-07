from src.entity.job_description import JobDescription
from src.entity.match_result import MatchResult
from src.entity.resume import Resume
from src.reporting.report_generator import ReportGenerator


def test_report_generator():

    resume = Resume(
        skills=[
            "Python",
            "SQL",
            "Docker",
        ],
        experience_years=4,
    )

    job = JobDescription(
        skills=[
            "Python",
            "SQL",
            "Docker",
            "AWS",
        ],
        experience_years=5,
    )

    match = MatchResult(
        overall_score=0.88,
        rule_based_score=0.86,
        tfidf_score=0.89,
        semantic_score=0.90,
        skill_score=0.75,
        experience_score=0.80,
        missing_skills=["AWS"],
    )

    generator = ReportGenerator()

    report = generator.generate(
        resume,
        job,
        match,
    )

    assert report.overall_score == 0.88

    assert report.matched_skills == [
        "Python",
        "SQL",
        "Docker",
    ]

    assert report.missing_skills == [
        "AWS",
    ]

    assert report.experience_gap == 1

    assert report.recommendation == "Consider learning: AWS"