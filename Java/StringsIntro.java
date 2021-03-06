import java.io.*;
import java.util.*;

public class StringsIntro {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        System.out.println(A.length() + B.length());
        System.out.println(A.compareTo(B) > 0 ? "Yes" : "No");
        System.out.println(Capitalizer(A) + " " + Capitalizer(B));
    }
    
    public static String Capitalizer(String s) {
        if (s == null || s.length() == 0)
            return s;
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }
}
