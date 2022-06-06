from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def print(self) -> None:
        pass
