from .base import Beverage


class Tee(Beverage):
    def prepare(self):
        print("Prepearing a tee.")
        super().prepare()

    def drink(self):
        print(
            f"Drinking {self.supplement.name} tee with {self.sugar} sugar {self.serving.SERVING_NAME}s."
        )

    def cost(self):
        return 7 + self.supplement.add_cost()
