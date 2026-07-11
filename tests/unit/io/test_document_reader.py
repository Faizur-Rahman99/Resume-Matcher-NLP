from src.io.document_reader import DocumentReader


def test_read_txt():

    reader = DocumentReader()

    text = reader.read("tests/data/sample_resume.txt")

    assert isinstance(text, str)
    assert "Python" in text
    assert "Docker" in text
    assert "3 years" in text


def test_read_pdf():

    reader = DocumentReader()

    text = reader.read("tests/data/sample_resume.pdf")

    assert isinstance(text, str)
    assert "Python" in text
    assert "Docker" in text
    assert "3 years" in text


def test_read_docx():

    reader = DocumentReader()

    text = reader.read("tests/data/sample_resume.docx")

    assert isinstance(text, str)
    assert "Python" in text
    assert "Docker" in text
    assert "3 years" in text