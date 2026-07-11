from src.components.name_extractor import NameExtractor


extractor = NameExtractor()


def test_extract_simple_name():

    text = """
    John Doe

    Software Engineer

    john@example.com
    """

    assert extractor.extract(text) == "John Doe"


def test_extract_md_name():

    text = """
    Md. Faizur Rahman

    Backend Developer

    faizur@gmail.com
    """

    assert extractor.extract(text) == "Md. Faizur Rahman"


def test_extract_uppercase_name():

    text = """
    MUHAMMAD FAIZUR RAHMAN

    AI Engineer

    faizur@gmail.com
    """

    assert extractor.extract(text) == "MUHAMMAD FAIZUR RAHMAN"


def test_extract_name_before_email():

    text = """
    Jane Smith

    Email:
    jane@gmail.com
    """

    assert extractor.extract(text) == "Jane Smith"


def test_no_name_found():

    text = """
    Email:
    abc@gmail.com

    Skills:
    Python
    Docker
    """

    assert extractor.extract(text) is None