import re


class EducationExtractor:

    PATTERNS = [
        r".*\bBSc\b.*",
        r".*\bBachelor\b.*",
        r".*\bMSc\b.*",
        r".*\bMaster\b.*",
        r".*\bPhD\b.*",
    ]

    def extract(self, text: str) -> list[str]:

        education = []

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            for pattern in self.PATTERNS:

                if re.search(
                    pattern,
                    line,
                    re.IGNORECASE,
                ):
                    education.append(line)
                    break

        return education