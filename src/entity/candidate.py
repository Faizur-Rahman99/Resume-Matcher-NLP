from dataclasses import dataclass

from src.entity.match_result import MatchResult
from src.entity.resume import Resume


@dataclass
class Candidate:
    resume: Resume
    match_result: MatchResult