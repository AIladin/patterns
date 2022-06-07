from .base import BaseListener


class MaxLengthListener(BaseListener):
    def __init__(self):
        self.max_length = 0
        self.line = None

    def update(self, line: str):
        line_len = len(line)
        if line_len > self.max_length:
            print(f"Found new longest line: {line_len} chars.")
            self.max_length = line_len
            self.line = line
