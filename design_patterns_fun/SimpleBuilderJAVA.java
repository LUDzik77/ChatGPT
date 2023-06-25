class Pizza {
    private String size;
    private boolean doubleCheese;
    private boolean pepperoni;
    private boolean mushrooms;

    public Pizza() {
        size = null;
        doubleCheese = false;
        pepperoni = false;
        mushrooms = false;
    }

    //here we override method of string class  ~__str__ python
    @Override
    public String toString() {
        return String.format("Size: %s, cheeseX2: %s, Pepperoni: %s, Mushrooms: %s",
                size, doubleCheese, pepperoni, mushrooms);
    }

    public void setSize(String size) {
        this.size = size;
    }

    public void addCheese() {
        doubleCheese = true;
    }

    public void addPepperoni() {
        pepperoni = true;
    }

    public void addMushrooms() {
        mushrooms = true;
    }
}

class PizzaBuilder {
    private Pizza pizza;

    public PizzaBuilder() {
        pizza = new Pizza();
    }

    public PizzaBuilder setSize(String size) {
        pizza.setSize(size);
        return this;
    }

    public PizzaBuilder addCheese() {
        pizza.addCheese();
        return this;
    }

    public PizzaBuilder addPepperoni() {
        pizza.addPepperoni();
        return this;
    }

    public PizzaBuilder addMushrooms() {
        pizza.addMushrooms();
        return this;
    }

    public Pizza build() {
        return pizza;
    }
}

public class main {
    public static void main(String[] args) {
        PizzaBuilder pizzaBuilder = new PizzaBuilder();
        Pizza pizza = pizzaBuilder.setSize("Large").addCheese().addMushrooms().build();
        System.out.println(pizza);
    }
}