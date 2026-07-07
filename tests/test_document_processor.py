import pytest

from src.io.document_processor import DocumentProcessor


@pytest.mark.parametrize(
    "path",
    [
        "tests/data/sample_resume.txt",
        "tests/data/sample_resume.pdf",
        "tests/data/sample_resume.docx",
    ],
)
def test_document_processor(path):

    processor = DocumentProcessor()

    resume = processor.process(path)

    assert "Python" in resume.skills
    assert "Docker" in resume.skills
    assert resume.experience_years == 5