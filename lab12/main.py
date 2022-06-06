from car.car import Car, CarBuilder, Color, CarType
from car import compounds


def main():
    print("Building 100 default cars")
    car_builder = CarBuilder()
    # single instance of default engine and default wheels will be created
    default_cars = [car_builder.build() for i in range(100)]

    # cars which only differs from default cars in color and type
    # no new engines and wheels will be created
    print("Building 100 cars with different color and style")
    car_builder.set_color(Color.BLACK)
    car_builder.set_type(CarType.HATCHBACK)
    type_1_cars = [car_builder.build() for i in range(100)]

    # cars with different wheels and engiens
    # one instace of wheel and one instance of engine will be created
    print("Building 100 cars whith different engine and wheels")
    car_builder.set_engine(15, compounds.Fuel.DIESEL)
    car_builder.set_wheel(10, compounds.WheelMaterial.STEEL)
    type_2_cars = [car_builder.build() for i in range(100)]


if __name__ == "__main__":
    main()
