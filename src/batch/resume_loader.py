from pathlib import Path


class ResumeLoader:

    SUPPORTED_EXTENSIONS = {
        ".txt",
        ".pdf",
        ".docx",
    }

    def load(self, folder: str) -> list[Path]:

        folder = Path(folder)

        resumes = [
            file
            for file in folder.iterdir()
            if file.is_file()
            and file.suffix.lower() in self.SUPPORTED_EXTENSIONS
        ]

        return sorted(resumes)