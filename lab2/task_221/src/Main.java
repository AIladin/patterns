import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<CoffeeFactory> coffeeFactories = new ArrayList<>();
        coffeeFactories.add(new AmericanoFactory());
        coffeeFactories.add(new CappuccinoFactory());
        coffeeFactories.add(new EspressoFactory());
        coffeeFactories.add(new LatteFactory());
        coffeeFactories.add(new RafFactory());

        ArrayList<Coffee> coffees = new ArrayList<>();
        for (CoffeeFactory coffeeFactory : coffeeFactories) {
            for (int i = 0; i < 15; i++) {
                Coffee coffee = coffeeFactory.create();
                coffees.add(coffee);
            }
        }

        float totalProfit = coffees.stream().map(Coffee::profit).reduce(0.f, Float::sum);
        System.out.printf("Total Profit: %f%n", totalProfit);
    }

}
