from abc import ABC, abstractmethod


class Bevrage(ABC):
    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def cost(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Bevrage: {self.description}, ${self.cost:.2f}"
