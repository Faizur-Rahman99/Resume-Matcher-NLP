from src.entity.job_description import JobDescription
from src.entity.resume import Resume
from src.matching.resume_ranker import ResumeRanker


def test_resume_ranker():

    resumes = [

        Resume(
            skills=["Python", "SQL", "Docker"],
            experience_years=4
        ),

        Resume(
            skills=["Python"],
            experience_years=1
        ),

        Resume(
            skills=["Python", "SQL", "Docker", "AWS"],
            experience_years=8
        )
    ]

    job = JobDescription(
        skills=["Python", "SQL", "Docker", "AWS"],
        experience_years=5
    )

    ranker = ResumeRanker()

    ranked = ranker.rank(resumes, job)

    assert len(ranked) == 3
    assert ranked[0].match_result.overall_score >= ranked[1].match_result.overall_score
    assert ranked[1].match_result.overall_score >= ranked[2].match_result.overall_score