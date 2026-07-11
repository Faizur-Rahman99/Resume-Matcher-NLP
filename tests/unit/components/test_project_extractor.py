from src.components.project_extractor import ProjectExtractor


extractor = ProjectExtractor()


def test_single_project():

    text = """
    Projects

    AI Resume Matcher
    """

    assert extractor.extract(text) == [
        "AI Resume Matcher"
    ]


def test_multiple_projects():

    text = """
    Projects

    AI Resume Matcher

    Customer Churn Prediction

    E-commerce Website
    """

    assert extractor.extract(text) == [
        "AI Resume Matcher",
        "Customer Churn Prediction",
        "E-commerce Website",
    ]


def test_no_projects():

    text = """
    Skills

    Python
    Docker
    """

    assert extractor.extract(text) == []