from typing import List


class NGramGenerator:

    @staticmethod
    def generate(tokens: List[str], n: int) -> List[str]:
        
        if n <= 0:
            raise ValueError("n must be greater than 0")

        if len(tokens) < n:
            return []

        return [
            " ".join(tokens[i:i + n])
            for i in range(len(tokens) - n + 1)
        ]