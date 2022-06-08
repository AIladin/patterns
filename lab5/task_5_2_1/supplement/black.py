from .base import Supplement


class Black(Supplement):
    def __init__(self):
        super().__init__("black")

    def add_supplement(self):
        print("Making your bevrage darker.")

    def add_cost(self):
        return 3
