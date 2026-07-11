class SkillMatcher:
    """
    Calculates the proportion of required skills present in a resume.
    """

    def match(
        self,
        resume_skills: list[str],
        required_skills: list[str],
    ) -> float:
        """
        Compute a skill match score between 0.0 and 1.0.
        """

        if not required_skills:
            return 0.0

        resume_skill_set = {
            skill.lower()
            for skill in resume_skills
        }

        required_skill_set = {
            skill.lower()
            for skill in required_skills
        }

        matched_skills = (
            resume_skill_set &
            required_skill_set
        )

        return (
            len(matched_skills) /
            len(required_skill_set)
        )