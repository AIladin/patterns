from .base import BaseListener


class WordCounterListener(BaseListener):
    def __init__(self):
        self.word_count = 0

    def update(self, line: str):
        self.word_count += len(line.split())
