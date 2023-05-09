package org.example;
import java.util.Scanner;


public class Triangle_task {
    public static void main(String[] args) throws Exception
    {
    System.out.println("Enter the sides of your triangle:");
    int a, b, c;
    Scanner scanner = new Scanner(System.in);
    System.out.print("a=");
    a = scanner.nextInt();
    System.out.print("b=");
    b = scanner.nextInt();
    System.out.print("c=");
    c = scanner.nextInt();


    if (a<b+c && b<a+c && c<a+b)
    {
        System.out.println("CORRECT sides of a triangle");
    }
    else
        System.out.println("CAN't build a triangle from the given sides");
    }

}
