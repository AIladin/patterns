from component import Component


class PrintableStrings(Component):
    def __init__(self, base: str):
        self.base = base

    def print(self) -> None:
        print(self.base, end="")
