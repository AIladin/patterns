from .base import BaseDecorator


class PostCommaDecorator(BaseDecorator):
    def print(self):
        super().print()
        print(", ", end="")
