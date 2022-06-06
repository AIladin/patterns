from abc import ABC, abstractproperty


class Bevrage(ABC):
    @abstractproperty
    def description(self) -> str:
        pass

    @abstractproperty
    def cost(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Bevrage: {self.description}, ${self.cost:.2f}"
