import java.io.*;
import java.util.*;

public class StringReverse {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String s= "";
        for (int i = A.length() - 1; i > -1; i--) {
            s += A.charAt(i);
        }
        
        if (A.compareTo(s) == 0) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}
