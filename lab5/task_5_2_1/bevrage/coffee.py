from .base import Beverage


class Coffee(Beverage):
    def prepare(self):
        print("Prepearing coffee.")
        super().prepare()

    def drink(self):
        print(
            f"Drinking {self.supplement.name} coffee with {self.sugar} sugar {self.serving.SERVING_NAME}s."
        )

    def cost(self):
        return 10 + self.supplement.add_cost()
