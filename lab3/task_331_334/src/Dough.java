public class Dough {
    public enum FlourType{
        RYE,
        WHEAT,
        CORN
    }

    public enum DoughType{
        THIN,
        NORMAL
    }
    private final FlourType flourType;
    private final DoughType doughType;

    public Dough(FlourType flourType, DoughType doughType){
        this.doughType = doughType;
        this.flourType = flourType;
    }

    public FlourType getFlourType() {
        return flourType;
    }

    public DoughType getDoughType() {
        return doughType;
    }

    @Override
    public String toString() {
        return "Dough {type=" + doughType + ", flour=" + flourType + "}";
    }
}
