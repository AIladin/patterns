from abc import ABC, abstractmethod


class Supplement(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add_supplement(self):
        pass

    @abstractmethod
    def add_cost(self):
        pass
