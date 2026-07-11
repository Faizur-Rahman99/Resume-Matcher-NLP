from fastapi import FastAPI

from src.api.routes import router


app = FastAPI(
    title="Resume Matcher API",
    description=(
        "API for parsing resumes, extracting skills, "
        "and ranking candidates against job descriptions."
    ),
    version="1.0.0",
)

app.include_router(router)