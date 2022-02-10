public class EspressoFactory extends CoffeeFactory {
    @Override
    public Coffee create() {
        return new Espresso();
    }
}
