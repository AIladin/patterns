public class Main {
    public static void main(String[] args) {
        Auto truck = new Auto(10, "Ford", true, 1000);
        Auto car = new Auto(1, "Tesla", false, 100);
        CarCustomsAdapter carCustomsAdapter = new CarCustomsAdapter(29.55f, 0.10f);
        TruckCustomsAdapter truckCustomsAdapter = new TruckCustomsAdapter(29.55f, 0.10f);
        System.out.println("Car price: " + carCustomsAdapter.vehiclePrice(car) + " tax: " + carCustomsAdapter.tax(car));
        System.out.println("Truck price: " + truckCustomsAdapter.vehiclePrice(truck) + " tax: " + truckCustomsAdapter.tax(truck));
    }
}
