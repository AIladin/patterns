from abc import ABC, abstractmethod

from serving.base import Serving
from supplement.base import Supplement


class Beverage(ABC):
    def __init__(
        self,
        sugar: int,
        supplement: Supplement,
        water_volume: int,
        serving: Serving,
    ):
        self.sugar = sugar
        self.supplement = supplement
        self.water_volume = water_volume
        self.serving = serving

    def prepare(self):
        if self.supplement:
            self.supplement.add_supplement()
        print(f"Adding {self.water_volume} hot water.")
        if self.sugar > 0:
            print(f"Adding {self.sugar} pieces of sugar.")
        self.serving.serve()

    @abstractmethod
    def drink(self):
        pass

    @property
    @abstractmethod
    def cost(self):
        pass
