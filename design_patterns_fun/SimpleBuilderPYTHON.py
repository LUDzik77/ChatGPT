class Pizza:
    def __init__(self):
        self.size = None
        self.double_cheese = False
        self.pepperoni = False
        self.mushrooms = False

    def __str__(self):
        return f"Size: {self.size}, cheeseX2: {self.double_cheese}, Pepperoni: {self.pepperoni}, Mushrooms: {self.mushrooms}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.double_cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def build(self):
        return self.pizza


#Usage 1:
pizza_builder = PizzaBuilder()
pizza = pizza_builder.set_size("Large").add_cheese().add_mushrooms().build()
print(pizza)
