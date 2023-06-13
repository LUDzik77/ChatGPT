package org.example;

class Shape {
    protected String shape;
    public void draw() {
        System.out.println("Drawing a " + shape);
    }
}

class Circle extends Shape {
    //String shape = "circle"; //won't work --> give "null
    public Circle() {
        shape = "Circle";
    }
}

class Rectangle extends Shape {
    public Rectangle() {
        shape = "rectangle";
    }
}

class ShapeFactory {
    public Shape createShape(String givenShape) {
        if (givenShape.equals("circle")) {
            return new Circle();
        } else if (givenShape.equals("rectangle")) {
            return new Rectangle();
        } else {
            throw new IllegalArgumentException("Invalid shape type");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        ShapeFactory factory = new ShapeFactory();
        Shape circle = factory.createShape("circle");
        circle.draw();
        Shape rectangle = factory.createShape("rectangle");
        rectangle.draw();
    }
}