
https://www.codechef.com/problems/TCG

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int x = scanner.nextInt();
        int y = scanner.nextInt();

        int difference = x - y;

        if (difference > 0) {
            System.out.println("DECREASED");
        } else if (difference < 0) {
            System.out.println("INCREASED");
        } else {
            System.out.println("SAME");
        }
    }
}