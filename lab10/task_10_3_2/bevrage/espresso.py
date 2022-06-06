from .base import Bevrage


class Espresso(Bevrage):
    @property
    def description(self) -> str:
        return "Espresso"

    @property
    def cost(self) -> float:
        return 0.75
