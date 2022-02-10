public class RafFactory extends CoffeeFactory {
    @Override
    public Coffee create() {
        return new Raf();
    }
}
