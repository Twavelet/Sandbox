import java.util.Objects;
import java.util.Scanner;
import java.util.stream.IntStream;

public abstract class Main {
    static void checkPassword() {
        Scanner password = new Scanner(System.in);
        System.out.println("Enter your password: ");
        String userPassword = password.nextLine();
        String validated;
        if (userPassword != "") {
            do {
                Scanner passwordValidation = new Scanner(System.in);
                System.out.println("Re-enter your password for confirmation: ");
                validated = passwordValidation.nextLine();
            }
            while (!Objects.equals(validated, userPassword));
//        Objects.equals(value, value) -> better used than !==

        } else {
            checkPassword();
        }
    }
    public static void main(String[] args) {
//       Loops Refresher Lab:

//      #1
        for (int a = 0; a < 5; a++) {
            System.out.println("Hello");
        }

//      #2
        for (int b = 0; b < 11; b++) {
            System.out.println(b);
        }

//      #3
        for (int c = 10; c >= 0; c--) {
            System.out.println(c);
        }

//      #4
        Scanner userInput = new Scanner(System.in);
        System.out.println("How many times do you want to iterate?");
        int iterations = userInput.nextInt();
        System.out.println(iterations);
        for (int d = 0; d < iterations; d++) {
            System.out.println("Interested logic flow here");
        }

//      #5
        String word = "Printable";
        for (int e = 0; e < word.length(); e++) {
            System.out.println(word.charAt(e));
        }

//      #6
        for (int f = 0; f < 101; f++) {
            if (f % 3 == 0 && f % 5 == 0) {
                System.out.println("FizzBuzz");
            } else if (f % 3 == 0) {
                System.out.println("Fizz");
            } else if (f % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(f);
            }
        }

//      #7
        int g = 0;
        do {
            System.out.println("Doing");
            g++;
        }
        while (g < 5);

        //    #8
        checkPassword();
    }




}
