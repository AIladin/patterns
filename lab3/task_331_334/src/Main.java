public class Main {
    public static void main(String[] args) {
        Pizzaiolo director = Pizzaiolo.getInstance("Pizzaiolo");
        Pizzaiolo director1 = Pizzaiolo.getInstance("Singleton test");

        Pizza pepperoni = director.pepperoni();
        System.out.println(pepperoni);

        Pizza vegan = director.vegan();
        System.out.println(vegan);
    }
}
