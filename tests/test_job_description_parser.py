from src.components.job_description_parser import JobDescriptionParser


def test_job_description_parser():

    parser = JobDescriptionParser()

    text = """
    We are looking for a Data Scientist with 3 years of experience.
    Required skills: Python, SQL Server, Docker.
    """

    job = parser.parse(text)

    assert "Python" in job.skills
    assert "Docker" in job.skills
    assert job.experience_years == 3