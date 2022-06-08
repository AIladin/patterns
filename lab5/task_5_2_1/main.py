import bevrage
import serving
import supplement
from bevrage.base import Beverage


def prepare_and_drink(beverage: Beverage):
    beverage.prepare()
    print("Cost of beverage:", beverage.cost())
    beverage.drink()
    print()


def main():
    black_coffee = bevrage.Coffee(0, supplement.Black(), 1, serving.Indoor())
    prepare_and_drink(black_coffee)

    coffie_with_milk = bevrage.Coffee(2, supplement.Milk(0.5), 1, serving.Indoor())
    prepare_and_drink(coffie_with_milk)

    black_tee = bevrage.Tee(0, supplement.Black(), 2, serving.Outdoor())
    prepare_and_drink(black_tee)

    milk_tee = bevrage.Tee(2, supplement.Milk(0.5), 2, serving.Indoor())
    prepare_and_drink(milk_tee)

    black_chocolate = bevrage.Chocolate(0, supplement.Black(), 1, serving.Outdoor())
    prepare_and_drink(black_chocolate)

    milk_chocolate = bevrage.Chocolate(2, supplement.Milk(1), 2, serving.Indoor())
    prepare_and_drink(milk_chocolate)


if __name__ == "__main__":
    main()
