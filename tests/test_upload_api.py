from fastapi.testclient import TestClient

from src.api.app import app


client = TestClient(app)


def test_upload_resume():

    with open(
        "tests/data/sample_resume.txt",
        "rb",
    ) as file:

        response = client.post(
            "/upload",
            files={
                "file": (
                    "sample_resume.txt",
                    file,
                    "text/plain",
                )
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert "Python" in data["skills"]
    assert "Docker" in data["skills"]
    assert data["experience_years"] == 5