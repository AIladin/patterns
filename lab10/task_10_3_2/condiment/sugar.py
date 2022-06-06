from .base import CondimentDecorator


class SugarDecorator(CondimentDecorator):
    @property
    def description(self) -> str:
        return self.bevrage.description + ", Sugar"

    @property
    def cost(self) -> float:
        return self.bevrage.cost + 0.1
