package org.example;

public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return this.age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void celebrateBirthday() {
        this.age++;
        System.out.println(this.name + " is now " + this.age + " years old!");
    }

    public static void main(String[] args) {
        Person Andrzej = new Person("Andrzej", 25);
        Person Adam = new Person("Adam", 30);

        Andrzej.celebrateBirthday();
        Adam.celebrateBirthday();
        Andrzej.celebrateBirthday();
        Adam.celebrateBirthday();

        Adam.setName("Ewa");
        Andrzej.setAge(40);

        System.out.println(Adam.getName() + " is " + Adam.getAge() + " years old.");
        System.out.println(Andrzej.getName() + " is " + Andrzej.getAge() + " years old.");
    }
}
