from src.entity.match_report import MatchReport


class ReportGenerator:

    def generate(self, resume, job, match):

        matched_skills = [
            skill
            for skill in resume.skills
            if skill in job.skills
        ]

        experience_gap = (
            job.experience_years
            - resume.experience_years
        )

        if match.missing_skills:
            recommendation = (
                "Consider learning: "
                + ", ".join(match.missing_skills)
            )
        else:
            recommendation = "Excellent match."

        return MatchReport(
            overall_score=match.overall_score,
            matched_skills=matched_skills,
            missing_skills=match.missing_skills,
            experience_gap=experience_gap,
            recommendation=recommendation,
        )