from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    summary="Health check",
)
def health():

    return {
        "status": "healthy",
        "message": "Resume Matcher API is running",
    }