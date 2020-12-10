import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ContentExtractor{
	public static void main(String[] args){
		
		Scanner input = new Scanner(System.in);
		int testCases = Integer.parseInt(input.nextLine());
		
        while(testCases > 0){
			String line = input.nextLine();
			
          	boolean matched = false;
            Pattern reg_expr = Pattern.compile("<(.+)>([^<]+)</\\1>");
            Matcher compare = reg_expr.matcher(line);
            
            while (compare.find()) {
                System.out.println(compare.group(2));
                matched = true;
            }
            
            if (!matched)
                System.out.println("None");
			
			testCases--;
		}
	}
}
