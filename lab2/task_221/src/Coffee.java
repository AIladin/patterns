abstract public class Coffee {
    public abstract float getSellCost();

    public abstract float getSelfCost();

    public float profit() {
        return this.getSellCost() - this.getSelfCost();
    }

}
