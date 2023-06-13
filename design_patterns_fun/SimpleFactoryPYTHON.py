class Shape:
    shape = "n/a"
    def draw(cls):
        print(f"Drawing a {cls.shape}")

class Circle(Shape):
    shape = "circle"

class Rectangle(Shape):
    shape = "rectangle"

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Invalid shape type")


factory = ShapeFactory()

circle = factory.create_shape("circle")
print(circle.shape)
circle.draw()  

rectangle = factory.create_shape("rectangle")
rectangle.draw() 