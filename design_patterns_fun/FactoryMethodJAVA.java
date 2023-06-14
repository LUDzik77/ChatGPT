package org.example;

// interfaces can be "inherited" from ; no functions body
// remember: a class can inherit only 1 master class
//           but implements more than 1 interface (no idea if it is useful)

interface Animal {
    String speak();
}

class Dog implements Animal {
    @Override
    public String speak() {
        return "Woof!";
    }
}

class Cat implements Animal {
    @Override
    public String speak() {
        return "Meow!";
    }
}

class DogFactory {
    public Animal createAnimal() {
        return new Dog();
    }
}

class CatFactory {
    public Animal createAnimal() {
        return new Cat();
    }
}

class AnimalLocalFactory {
    private static boolean hasDog = false;

    public Animal createAnimal() {
        if (!hasDog) {
            hasDog = true;
            return new Dog();
        } else {
            return new Cat();
        }
    }
}


public class Main {
    public static void main(String[] args) {
        DogFactory dogFactory = new DogFactory();
        Animal dog = dogFactory.createAnimal();
        System.out.println(dog.speak());

        CatFactory catFactory = new CatFactory();
        Animal cat = catFactory.createAnimal();
        System.out.println(cat.speak());

        AnimalLocalFactory alf = new AnimalLocalFactory();
        String x = alf.createAnimal().speak();
        String y = alf.createAnimal().speak();
        System.out.println(x + " " + y);

        //Animals have interface, but ALF does not
        //We could add it as well as f.e AnimalFactory
        AnimalLocalFactory alf2 = new AnimalLocalFactory();
        Animal dog_or_cat =  alf2.createAnimal();
        System.out.println(dog_or_cat.speak());
    }
}