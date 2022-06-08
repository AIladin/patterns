from .base import Beverage


class Chocolate(Beverage):
    def prepare(self):
        print("Prepearing cacao.")
        super().prepare()

    def drink(self):
        print(
            f"Drinking {self.supplement.name} chocolate with {self.sugar} sugar {self.serving.SERVING_NAME}s."
        )

    def cost(self):
        return 15 + self.supplement.add_cost()
