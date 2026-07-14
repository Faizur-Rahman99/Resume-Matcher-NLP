from src.entity.match_result import MatchResult
from src.entity.resume import Resume
from src.entity.job_description import JobDescription
from src.matching.experience_matcher import ExperienceMatcher
from src.matching.skill_matcher import SkillMatcher
from src.ml.tfidf_similarity import TFIDFSimilarity
from src.matching.explanation_engine import ExplanationEngine

from src.config.scoring import (
    EXPERIENCE_WEIGHT,
    RULE_BASED_WEIGHT,
    SEMANTIC_WEIGHT,
    SKILL_WEIGHT,
    TFIDF_WEIGHT,
)

import os

class SimilarityEngine:

    def __init__(self):
        self.skill_matcher = SkillMatcher()
        self.experience_matcher = ExperienceMatcher()
        self.tfidf = TFIDFSimilarity()

        self.use_semantic = (
                os.getenv("USE_SEMANTIC", "true").lower() == "true"
        )

        if self.use_semantic:
            from src.ml.semantic_similarity import SemanticSimilarity
            self.semantic = SemanticSimilarity()

        self.explanation_engine = ExplanationEngine()

    def match(
        self,
        resume: Resume,
        job: JobDescription
    ) -> MatchResult:

        skill_score = self.skill_matcher.match(
            resume.skills,
            job.skills
        )

        experience_score = self.experience_matcher.match(
            resume.experience_years,
            job.experience_years
        )

        rule_based_score = round(
            skill_score * SKILL_WEIGHT +
            experience_score * EXPERIENCE_WEIGHT,
            3
        )

        resume_text = " ".join(resume.skills)
        job_text = " ".join(job.skills)

        tfidf_score = self.tfidf.calculate(
            resume_text,
            job_text
        )

        if self.use_semantic:
            semantic_score = self.semantic.calculate(
                resume_text,
                job_text
            )
        else:
            semantic_score = 0.0

        if self.use_semantic:

            overall_score = round(
                rule_based_score * RULE_BASED_WEIGHT
                + tfidf_score * TFIDF_WEIGHT
                + semantic_score * SEMANTIC_WEIGHT,
                3
            )

        else:

            total_weight = (
                    RULE_BASED_WEIGHT +
                    TFIDF_WEIGHT
            )

            overall_score = round(
                (
                        rule_based_score * RULE_BASED_WEIGHT
                        + tfidf_score * TFIDF_WEIGHT
                ) / total_weight,
                3
            )

        matched_skills = sorted(
            set(resume.skills) & set(job.skills)
        )

        missing_skills = sorted(
            set(job.skills) - set(resume.skills)
        )

        result = MatchResult(
            overall_score=overall_score,
            rule_based_score=rule_based_score,
            tfidf_score=tfidf_score,
            semantic_score=semantic_score,
            skill_score=skill_score,
            experience_score=experience_score,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
        )

        result.explanation = self.explanation_engine.generate(
            resume,
            job,
            result,
        )

        return result