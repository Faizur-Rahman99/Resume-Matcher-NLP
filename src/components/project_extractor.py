class ProjectExtractor:

    HEADERS = {
        "projects",
        "personal projects",
        "academic projects",
    }

    STOP_HEADERS = {
        "education",
        "experience",
        "skills",
        "certifications",
        "languages",
        "contact",
    }

    def extract(self, text: str) -> list[str]:

        lines = [
            line.strip()
            for line in text.splitlines()
        ]

        projects = []

        inside = False

        for line in lines:

            lower = line.lower()

            if lower in self.HEADERS:
                inside = True
                continue

            if inside and lower in self.STOP_HEADERS:
                break

            if inside and line:
                projects.append(line)

        return projects