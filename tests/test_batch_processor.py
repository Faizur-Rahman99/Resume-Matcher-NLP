from src.batch.batch_processor import BatchProcessor
from src.entity.job_description import JobDescription


def test_batch_processor():

    job = JobDescription(
        skills=[
            "Python",
            "SQL",
            "Docker",
            "AWS",
        ],
        experience_years=5,
    )

    processor = BatchProcessor()

    results = processor.process(
        "tests/data/resumes",
        job,
    )

    assert len(results) == 3

    assert (
        results[0]["match"].overall_score
        >= results[1]["match"].overall_score
    )

    assert (
        results[1]["match"].overall_score
        >= results[2]["match"].overall_score
    )