import requests

from src.config.settings import API_URL


class APIClient:

    def __init__(self):

        self.base_url = API_URL

    def health(self):

        response = requests.get(
            f"{self.base_url}/health"
        )

        response.raise_for_status()

        return response.json()

    def match(
        self,
        resume,
        job,
    ):

        response = requests.post(
            f"{self.base_url}/match",
            json={
                "resume": resume,
                "job": job,
            },
        )

        response.raise_for_status()

        return response.json()

    def upload_resume(
            self,
            file,
    ):
        response = requests.post(
            f"{self.base_url}/upload/resume",
            files={
                "file": (
                    file.name,
                    file,
                    file.type,
                ),
            },
        )

        response.raise_for_status()

        return response.json()

    def upload_job(
            self,
            file,
    ):
        response = requests.post(
            f"{self.base_url}/upload/job",
            files={
                "file": (
                    file.name,
                    file,
                    file.type,
                ),
            },
        )

        response.raise_for_status()

        return response.json()

    def batch_match(
            self,
            job,
            resumes,
    ):
        response = requests.post(
            f"{self.base_url}/match/batch",
            json={
                "job": job,
                "resumes": resumes,
            },
        )

        response.raise_for_status()

        return response.json()