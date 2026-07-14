from pathlib import Path

from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
)
from src.api.schemas import (
    JobData,
    ResumeData,
)
from src.constants.api import UPLOAD_DIR
from src.io.document_processor import DocumentProcessor

router = APIRouter(tags=["Upload"])

processor = None


def get_processor():
    global processor

    if processor is None:
        processor = DocumentProcessor()

    return processor


async def save_upload(file: UploadFile) -> Path:
    """
    Save an uploaded file to the upload directory and return its path.
    """

    upload_path = Path(UPLOAD_DIR)
    upload_path.mkdir(parents=True, exist_ok=True)

    destination = upload_path / file.filename

    with destination.open("wb") as buffer:
        buffer.write(await file.read())

    return destination


@router.post(
    "/upload/resume",
    summary="Upload and parse a resume",
    response_model=ResumeData,
)
async def upload_resume(
    file: UploadFile = File(...),
) -> ResumeData:
    """
    Upload a resume and extract structured candidate information.
    """

    try:

        destination = await save_upload(file)

        resume = get_processor().process(
            str(destination)
        )

        return ResumeData(
            filename=file.filename,
            name=resume.name,
            email=resume.email,
            phone=resume.phone,
            education=resume.education,
            projects=resume.projects,
            skills=resume.skills,
            experience_years=resume.experience_years,
        )



    except Exception as exc:

        raise HTTPException(

            status_code=400,

            detail=f"Failed to process resume: {exc}",

        )


@router.post(
    "/upload/job",
    summary="Upload and parse a job description",
    response_model=JobData,
)
async def upload_job(
    file: UploadFile = File(...),
) -> JobData:
    """
    Upload a job description and extract required skills and experience.
    """

    try:

        destination = await save_upload(file)

        job = get_processor().process(
            str(destination)
        )

        return JobData(
            skills=job.skills,
            experience_years=job.experience_years,
        )



    except Exception as exc:

        raise HTTPException(

            status_code=400,

            detail=f"Failed to process job: {exc}",

        )