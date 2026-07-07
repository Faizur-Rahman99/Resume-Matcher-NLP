import re


class ExperienceExtractor:

    PATTERNS = [
        r"(\d+)\+?\s+years?",
        r"(\d+)\+?\s+yrs?",
        r"experience\s+of\s+(\d+)",
        r"(\d+)\s+years?\s+of\s+experience",
        r"over\s+(\d+)\s+years?"
    ]

    def extract(self, text: str) -> int | None:

        text = text.lower()

        for pattern in self.PATTERNS:

            match = re.search(pattern, text)

            if match:
                return int(match.group(1))

        return None