class SkillMatcher:

    def match(
        self,
        resume_skills: list[str],
        required_skills: list[str]
    ) -> float:

        if not required_skills:
            return 0.0

        resume = {skill.lower() for skill in resume_skills}
        required = {skill.lower() for skill in required_skills}

        matched = resume & required

        return len(matched) / len(required)