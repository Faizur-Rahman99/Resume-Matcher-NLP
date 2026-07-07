class ExperienceMatcher:

    def match(
        self,
        resume_years: int | None,
        required_years: int | None
    ) -> float:

        if required_years is None:
            return 1.0

        if resume_years is None:
            return 0.0

        if resume_years >= required_years:
            return 1.0

        return resume_years / required_years