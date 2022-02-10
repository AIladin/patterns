public class LatteFactory extends CoffeeFactory {
    @Override
    public Coffee create() {
        return new Latte();
    }
}
