from .base import BaseBuilder


class StringBuilder(BaseBuilder):
    def __init__(self):
        self.result: str = None
        self.reset()

    def reset(self):
        self.result = ""
        return self

    def append_substring(self, substring: str):
        self.result += substring
        return self

    def insert_substring(self, substring: str, position: int):
        assert 0 <= position < len(self.result)
        self.result = self.result[:position] + substring + self.result[position:]
        return self

    def get_result(self) -> str:
        return self.result
