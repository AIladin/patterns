from .base import BaseListener


class MaxWordLengthListener(BaseListener):
    def __init__(self):
        self.longest_word = ""
        self.source_line = None

    def update(self, line: str):
        longest_word = max(line.split(), key=len)

        if len(longest_word) > len(self.longest_word):
            print(f"Found new longest word: {longest_word}, {len(longest_word)} chars.")
            self.longest_word = longest_word
            self.source_line = line
