import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
//       Loops Refresher Lab:
        for (int a = 0; a < 5; a++){
            System.out.println("Hello");
        }

        for(int b = 0; b < 11; b++){
            System.out.println(b);
        }

        for (int c = 10; c>=0; c--){
            System.out.println(c);
        }

        Scanner userInput = new Scanner(System.in);
        System.out.println("How many times do you want to iterate?");
        int iterations = userInput.nextInt();
        System.out.println(iterations);
        for (int d = 0; d < iterations; d++){
            System.out.println("Interested logic flow here");
        }

        

    }
}