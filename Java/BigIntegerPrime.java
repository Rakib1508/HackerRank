import java.math.BigInteger; 
import java.util.Scanner; 

public class BigIntegerPrime {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String n = scanner.nextLine();
        BigInteger number = new BigInteger(n);
        if (number.isProbablePrime(1)) {
            System.out.println("prime");
        } else {
            System.out.println("not prime");
        }
        scanner.close();
    }
}
