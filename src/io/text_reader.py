class TextReader:

    def read(self, path: str) -> str:

        with open(path, "r", encoding="utf-8") as file:
            return file.read()