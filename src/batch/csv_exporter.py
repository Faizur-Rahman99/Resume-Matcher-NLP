import csv
from pathlib import Path


class CSVExporter:

    def export(
        self,
        results,
        output_path: str,
    ):

        output = Path(output_path)

        with output.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
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
            )

            for rank, result in enumerate(
                results,
                start=1,
            ):

                match = result["match"]

                writer.writerow(
                    [
                        rank,
                        result["filename"],
                        match.overall_score,
                        match.rule_based_score,
                        match.tfidf_score,
                        match.semantic_score,
                        match.skill_score,
                        match.experience_score,
                        ", ".join(match.missing_skills),
                    ]
                )