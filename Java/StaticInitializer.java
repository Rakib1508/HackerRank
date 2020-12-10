import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class StaticInitializer {

    static Scanner input = new Scanner(System.in);
    static int B = input.nextInt();
    static int H = input.nextInt();
    static boolean flag = true;
    
    static {
        try {
            if (B < 1 || H < 1) {
                flag = false;
                throw new Exception("Breadth and height must be positive");
            }
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }


    public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
    }
    
}
