from src.entity.job_description import JobDescription
from src.entity.match_result import MatchResult
from src.entity.resume import Resume


class ExplanationEngine:

    def generate(
        self,
        resume: Resume,
        job: JobDescription,
        match: MatchResult,
    ) -> list[str]:

        explanation = []

        # Skill summary
        if match.matched_skills:
            explanation.append(
                f"Matched {len(match.matched_skills)} required skill(s)."
            )

        if match.missing_skills:
            explanation.append(
                "Missing: "
                + ", ".join(match.missing_skills)
            )
        else:
            explanation.append(
                "Candidate has all required skills."
            )

        # Experience
        if resume.experience_years >= job.experience_years:
            explanation.append(
                "Meets the experience requirement."
            )
        else:
            difference = (
                job.experience_years
                - resume.experience_years
            )

            explanation.append(
                f"Needs {difference} more year(s) of experience."
            )

        # Overall score
        explanation.append(
            f"Overall compatibility score: {match.overall_score:.0%}"
        )

        return explanation