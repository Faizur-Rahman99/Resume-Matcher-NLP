from services.api import APIClient


def analyze_candidates(job_file, resume_files):
    """
    Upload the job description and resumes to the backend,
    then request a batch ranking.
    """

    client = APIClient()

    # Process job description
    job_data = client.upload_job(job_file)

    # Process resumes
    resume_data = []

    for resume_file in resume_files:

        resume = client.upload_resume(resume_file)

        resume["filename"] = resume_file.name

        resume_data.append(resume)

    # Get ranked candidates
    ranking = client.batch_match(
        job=job_data,
        resumes=resume_data,
    )

    return ranking