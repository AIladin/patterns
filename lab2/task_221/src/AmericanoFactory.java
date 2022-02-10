public class AmericanoFactory extends CoffeeFactory {
    @Override
    public Coffee create() {
        return new Americano();
    }
}
