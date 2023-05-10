public class Args_test {
    public static void main(String[] args) {

        System.out.println("Hello and welcome!");
        System.out.printf("Hello and welcome!");
		    //It let you run compiled soft with arguments f.e -->  Args_test  hej kurwa hej
        for (String arg : args) {
            System.out.println(arg);
			if (arg.equals("kurwa")) {
				System.out.println("nie przeklinaj padalcu");
			}
        }
    }
}

