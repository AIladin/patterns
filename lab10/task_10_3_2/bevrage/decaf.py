from .base import Bevrage


class Decaf(Bevrage):
    @property
    def description(self) -> str:
        return "Decaf"

    @property
    def cost(self) -> float:
        return 1.0
