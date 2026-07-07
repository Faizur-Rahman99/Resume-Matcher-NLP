from src.components.resume_parser import ResumeParser


def test_resume_parser():

    parser = ResumeParser()

    text = """
    Software Engineer with 5 years of experience.
    Skilled in Python, SQL Server, Docker and TensorFlow.
    """

    resume = parser.parse(text)

    assert "Python" in resume.skills
    assert "Docker" in resume.skills
    assert resume.experience_years == 5