from pathlib import Path

from src.batch.resume_loader import ResumeLoader


def test_resume_loader(tmp_path: Path):

    (tmp_path / "resume1.pdf").touch()
    (tmp_path / "resume2.docx").touch()
    (tmp_path / "resume3.txt").touch()
    (tmp_path / "image.png").touch()

    loader = ResumeLoader()

    files = loader.load(str(tmp_path))

    assert len(files) == 3

    assert files[0].name == "resume1.pdf"
    assert files[1].name == "resume2.docx"
    assert files[2].name == "resume3.txt"