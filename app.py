from pathlib import Path

from src.components.job_description_parser import JobDescriptionParser
from src.components.resume_parser import ResumeParser
from src.matching.similarity_engine import SimilarityEngine


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main():
    resume_text = read_file(Path("examples/sample_resume.txt"))
    job_text = read_file(Path("examples/sample_job_description.txt"))

    resume = ResumeParser().parse(resume_text)
    job = JobDescriptionParser().parse(job_text)

    result = SimilarityEngine().match(resume, job)

    print("\n========== Resume Match Report ==========\n")

    print(f"Overall Match Score : {result.overall_score * 100:.1f}%")
    print(f"Skill Score         : {result.skill_score * 100:.1f}%")
    print(f"Experience Score    : {result.experience_score * 100:.1f}%")

    matched = sorted(set(resume.skills) & set(job.skills))

    print("\nMatched Skills")
    print("-" * 14)

    for skill in matched:
        print(f"✓ {skill}")

    print("\nMissing Skills")
    print("-" * 14)

    for skill in result.missing_skills:
        print(f"✗ {skill}")


if __name__ == "__main__":
    main()