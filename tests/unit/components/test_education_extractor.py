from src.components.education_extractor import EducationExtractor


extractor = EducationExtractor()


def test_extract_single_degree():

    text = """
    Education

    BSc in Computer Science
    """

    assert extractor.extract(text) == [
        "BSc in Computer Science"
    ]


def test_extract_multiple_degrees():

    text = """
    Education

    BSc in Computer Science

    MSc in Artificial Intelligence
    """

    assert extractor.extract(text) == [
        "BSc in Computer Science",
        "MSc in Artificial Intelligence",
    ]


def test_extract_no_education():

    text = """
    Skills

    Python
    Docker
    """

    assert extractor.extract(text) == []