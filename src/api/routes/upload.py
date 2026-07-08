from pathlib import Path

from fastapi import APIRouter, File, UploadFile

from src.constants.api import UPLOAD_DIR
from src.io.document_processor import DocumentProcessor

router = APIRouter()
processor = DocumentProcessor()

@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    upload_path = Path(UPLOAD_DIR)

    upload_path.mkdir(
        exist_ok=True
    )

    destination = upload_path / file.filename

    with destination.open("wb") as buffer:

        buffer.write(
            await file.read()
        )

    resume = processor.process(
        str(destination)
    )

    return {
        "skills": resume.skills,
        "experience_years": resume.experience_years,
    }