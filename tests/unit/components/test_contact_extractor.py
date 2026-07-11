from src.components.contact_extractor import ContactExtractor


extractor = ContactExtractor()


def test_extract_email():

    text = """
    John Smith
    john.smith@gmail.com
    """

    assert (
        extractor.extract_email(text)
        == "john.smith@gmail.com"
    )


def test_extract_phone():

    text = """
    Phone: +8801712345678
    """

    assert (
        extractor.extract_phone(text)
        == "+8801712345678"
    )


def test_extract_email_not_found():

    text = """
    John Smith
    Software Engineer
    """

    assert (
        extractor.extract_email(text)
        is None
    )


def test_extract_phone_not_found():

    text = """
    John Smith
    Software Engineer
    """

    assert (
        extractor.extract_phone(text)
        is None
    )