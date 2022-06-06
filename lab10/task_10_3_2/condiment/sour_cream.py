from .base import CondimentDecorator


class SourCreamDecorator(CondimentDecorator):
    @property
    def description(self) -> str:
        return self.bevrage.description + ", Sour-Cream"

    @property
    def cost(self) -> float:
        return self.bevrage.cost + 0.4
