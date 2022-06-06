from car import compounds
from car.car import Car, CarBuilder, CarType, Color


def main():
    print("Building 100 default cars")
    car_builder = CarBuilder()
    # single instance of default engine and default wheels will be created
    default_cars = [car_builder.build() for i in range(100)]
    print(default_cars[0], "x", len(default_cars))
    print()

    # cars which only differs from default cars in color and type
    # no new engines and wheels will be created
    print("Building 100 cars with different color and style")
    car_builder.set_color(Color.BLACK)
    car_builder.set_type(CarType.HATCHBACK)
    type_1_cars = [car_builder.build() for i in range(100)]
    print(type_1_cars[0], "x", len(type_1_cars))
    print()

    # cars with different wheels and engiens
    # one instace of wheel and one instance of engine will be created
    print("Building 100 cars whith different engine and wheels")
    car_builder.set_engine(15, compounds.Fuel.DIESEL)
    car_builder.set_wheel(10, compounds.WheelMaterial.STEEL)
    type_2_cars = [car_builder.build() for i in range(100)]
    print(type_2_cars[0], "x", len(type_2_cars))


if __name__ == "__main__":
    main()
