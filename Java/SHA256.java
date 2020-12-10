import java.util.*;
import java.security.*;

public class SHA256 {

    public static void main(String[] args) throws NoSuchAlgorithmException {
        Scanner input = new Scanner(System.in);
        String line = input.nextLine();
        
        MessageDigest type = MessageDigest.getInstance("SHA-256");
        type.reset();
        type.update(line.getBytes());
        
        for (byte x : type.digest()) {
            System.out.print(String.format("%02x", x));
        }
    }
}
