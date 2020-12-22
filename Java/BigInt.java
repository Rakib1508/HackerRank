import java.math.BigInteger;
import java.util.Scanner;

public class BigInt {
    public static void main (String[] args) {
        Scanner input = new Scanner(System.in);
        BigInteger num1 = new BigInteger(input.next());
        BigInteger num2 = new BigInteger(input.next());
        
        System.out.println(num1.add(num2));
        System.out.println(num1.multiply(num2));
    }
}