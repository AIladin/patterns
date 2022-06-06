from .base import CondimentDecorator


class CreamDecorator(CondimentDecorator):
    @property
    def description(self) -> str:
        return self.bevrage.description + ", Cream"

    @property
    def cost(self) -> float:
        return self.bevrage.cost + 0.4
