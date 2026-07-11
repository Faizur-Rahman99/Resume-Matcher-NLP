from fastapi.testclient import TestClient

from src.api.app import app


client = TestClient(app)


def test_match():

    response = client.post(
        "/match",
        json={
            "resume": {
                "skills": [
                    "Python",
                    "SQL",
                    "Docker",
                ],
                "experience_years": 4,
            },
            "job": {
                "skills": [
                    "Python",
                    "SQL",
                    "Docker",
                    "AWS",
                ],
                "experience_years": 5,
            },
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["matched_skills"] == [
        "Docker",
        "Python",
        "SQL",
    ]

    data = response.json()

    assert data["skill_score"] == 0.75
    assert data["experience_score"] == 0.8
    assert "AWS" in data["missing_skills"]

    assert 0 <= data["overall_score"] <= 1
    assert 0 <= data["rule_based_score"] <= 1
    assert 0 <= data["tfidf_score"] <= 1
    assert 0 <= data["semantic_score"] <= 1