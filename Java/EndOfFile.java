import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class EndOfFile {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int i = 1;
        while (input.hasNext()) {
            System.out.println(i + " " + input.nextLine());
            i++;
        }
        input.close();
    }
}
