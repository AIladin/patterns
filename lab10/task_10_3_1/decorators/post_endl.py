from .base import BaseDecorator


class PostEndlDeccorator(BaseDecorator):
    def print(self):
        super().print()
        print("\n", end="")
