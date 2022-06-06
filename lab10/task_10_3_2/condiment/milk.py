from .base import CondimentDecorator


class MilkDecorator(CondimentDecorator):
    @property
    def description(self) -> str:
        return self.bevrage.description + ", Milk"

    @property
    def cost(self) -> float:
        return self.bevrage.cost + 0.2
