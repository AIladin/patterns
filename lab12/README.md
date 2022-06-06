# Умова
12.2.2. Більшість автомобілів складається з великої кількості деталей таких як двигун, колеса, кермо тощо. Під час збірки автомобіля у нього встановлюють типові запчастини, що повторюються у багатьох модифікаціях. Відповідно, програмуючи деяку гру чи симулятор, що використовує подібні ієрархії класів можна суттєво заощадити оперативну пам’ять та зменшити час створення об’єктів класу Car, якщо закешувати однакові деталі.

# Результат
```
Building 100 default cars
Creating new engine. Engine(power=10, fuel=<Fuel.DIESEL: 'diesel'>)
Creating new wheel. Wheel(diameter=10, material=<WheelMaterial.ALLOY: 'alloy'>)
Car(car_type=<CarType.SEDAN: 'sedan'>, color=<Color.BLACK: 'black'>, engine=Engine(power=10, fuel=<Fuel.DIESEL: 'diesel'>), wheel=Wheel(diameter=10, material=<WheelMaterial.ALLOY: 'alloy'>)) x 100

Building 100 cars with different color and style
Car(car_type=<CarType.HATCHBACK: 'hatchback'>, color=<Color.BLACK: 'black'>, engine=Engine(power=10, fuel=<Fuel.DIESEL: 'diesel'>), wheel=Wheel(diameter=10, material=<WheelMaterial.ALLOY: 'alloy'>)) x 100

Building 100 cars whith different engine and wheels
Creating new engine. Engine(power=15, fuel=<Fuel.DIESEL: 'diesel'>)
Creating new wheel. Wheel(diameter=10, material=<WheelMaterial.STEEL: 'steel'>)
Car(car_type=<CarType.HATCHBACK: 'hatchback'>, color=<Color.BLACK: 'black'>, engine=Engine(power=15, fuel=<Fuel.DIESEL: 'diesel'>), wheel=Wheel(diameter=10, material=<WheelMaterial.STEEL: 'steel'>)) x 100
```