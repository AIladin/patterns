from .base import Bevrage


class DarkRoast(Bevrage):
    @property
    def description(self) -> str:
        return "DarkRoast"

    @property
    def cost(self) -> float:
        return 1.0
