from component import Component

from .base import BaseDecorator


class PostWordDecorator(BaseDecorator):
    def __init__(self, component: Component, word: str):
        super().__init__(component)
        self.word = word

    def print(self):
        super().print()
        print(self.word, end="")
