import csv

from src.batch.csv_exporter import CSVExporter
from src.entity.match_result import MatchResult


def test_csv_exporter(tmp_path):

    results = [
        {
            "filename": "resume1.txt",
            "match": MatchResult(
                overall_score=0.92,
                rule_based_score=0.90,
                tfidf_score=0.93,
                semantic_score=0.94,
                skill_score=0.85,
                experience_score=1.0,
                matched_skills=[
                    "Python",
                    "SQL",
                    "Docker",
                ],
                missing_skills=["AWS"],
            )
        },
        {
            "filename": "resume2.txt",
            "match": MatchResult(
                overall_score=0.80,
                rule_based_score=0.78,
                tfidf_score=0.81,
                semantic_score=0.82,
                skill_score=0.75,
                experience_score=0.90,
                matched_skills=[
                    "Python",
                    "SQL",
                ],
                missing_skills=["Docker"],
            )
        },
    ]

    output_file = tmp_path / "results.csv"

    exporter = CSVExporter()

    exporter.export(
        results,
        str(output_file),
    )

    assert output_file.exists()

    with output_file.open(
        newline="",
        encoding="utf-8",
    ) as file:

        rows = list(csv.reader(file))

    assert rows[0] == [
        "Rank",
        "Resume",
        "Overall Score",
        "Rule-Based Score",
        "TF-IDF Score",
        "Semantic Score",
        "Skill Score",
        "Experience Score",
        "Missing Skills",
    ]

    assert len(rows) == 3

    assert rows[1][0] == "1"
    assert rows[1][1] == "resume1.txt"
    assert rows[1][8] == "AWS"

    assert rows[2][0] == "2"
    assert rows[2][1] == "resume2.txt"
    assert rows[2][8] == "Docker"