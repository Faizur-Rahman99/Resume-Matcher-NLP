import re


class NameExtractor:

    def extract(self, text: str) -> str | None:

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        for line in lines[:5]:

            if "@" in line:
                continue

            if len(line.split()) < 2:
                continue

            if re.fullmatch(r"[A-Za-z.\- ]+", line):
                return line

        return None