from abc import ABC, abstractmethod


class DisplayObject(ABC):
    @abstractmethod
    def display(self):
        pass
