from .base import Supplement


class Milk(Supplement):
    def __init__(self, milk_volume: float):
        super().__init__("milk")
        self.milk_volume = milk_volume

    def add_supplement(self):
        print(f"Adding {self.milk_volume} milk.")

    def add_cost(self):
        return self.milk_volume * 3
