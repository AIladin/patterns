import bevrage
import condiment


def main():
    espresso_with_two_sugar = bevrage.Espresso()
    espresso_with_two_sugar = condiment.SugarDecorator(espresso_with_two_sugar)
    espresso_with_two_sugar = condiment.SugarDecorator(espresso_with_two_sugar)
    print(espresso_with_two_sugar)

    black_sour_cream_two_sugar = bevrage.DarkRoast()
    black_sour_cream_two_sugar = condiment.SugarDecorator(black_sour_cream_two_sugar)
    black_sour_cream_two_sugar = condiment.SugarDecorator(black_sour_cream_two_sugar)
    black_sour_cream_two_sugar = condiment.SourCreamDecorator(
        black_sour_cream_two_sugar
    )
    print(black_sour_cream_two_sugar)

    black_with_cream_and_sugar = bevrage.DarkRoast()
    black_with_cream_and_sugar = condiment.SugarDecorator(black_with_cream_and_sugar)
    black_with_cream_and_sugar = condiment.CreamDecorator(black_with_cream_and_sugar)
    print(black_with_cream_and_sugar)

    decaf_milk_two_sugar = bevrage.Decaf()
    decaf_milk_two_sugar = condiment.MilkDecorator(decaf_milk_two_sugar)
    decaf_milk_two_sugar = condiment.SugarDecorator(decaf_milk_two_sugar)
    decaf_milk_two_sugar = condiment.SugarDecorator(decaf_milk_two_sugar)
    print(decaf_milk_two_sugar)


if __name__ == "__main__":
    main()
