import java.io.*;
import java.util.*;

public class StringToken {

    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);
        String s=scan.nextLine();
        
        if (s.trim().length()==0 || s.trim().length()>4e5)
        {
            System.out.println(0);
            return;
        }

        String tokens[]=s.trim().split("[ !,?.\\_'@]+");
        System.out.println(tokens.length);
        
        for (String token : tokens)
            System.out.println(token);
    }
}

