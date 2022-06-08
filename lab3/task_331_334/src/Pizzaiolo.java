public class Pizzaiolo {

    private static Pizzaiolo instance;
    private final ConcreteBuilder builder = new ConcreteBuilder();
    private final String name;

    private Pizzaiolo(String name){
        this.name = name;
    }


    public static Pizzaiolo getInstance(String name){
        if (instance == null){
            System.out.println("Creating new pizzaiolo.");
            instance = new Pizzaiolo(name);
        }
        return instance;
    }

    @Override
    public String toString() {
        return name;
    }

    public Pizza vegan(){
        return builder.reset()
                .chooseDough(new Dough(Dough.FlourType.RYE, Dough.DoughType.THIN))
                .addIngredient(Pizza.Filling.OLIVES, 3)
                .getResult();
    }

    public Pizza pepperoni(){
        return builder.reset()
                .addIngredient(Pizza.Filling.SAUSAGES, 10)
                .addIngredient(Pizza.Filling.CHEESE, 15)
                .getResult();

    }
}
