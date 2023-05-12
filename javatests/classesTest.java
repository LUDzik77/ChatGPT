
public class Main {
    public static void main(String[] args) {
      // non-public classes inside the same Java file.
        class ClassA {
            public ClassA() {
                System.out.println("Class A");
            }
            public void mymethod() {
                System.out.println("the method of Class A");
            }
        }

        class ClassB {
            public ClassB() {
                System.out.println("Class B");
            }
        }
        System.out.println("start");
        ClassA c1 = new ClassA();
        ClassB c2 = new ClassB();
        c1.mymethod();

    }
}








