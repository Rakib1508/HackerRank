import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

class Regex{

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while(in.hasNext()){
            String IP = in.next();
            System.out.println(IP.matches(new MyRegex().pattern));
        }

    }
}

class MyRegex {
    String IPchecker = "(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])";
    public String pattern = String.format("%s.%s.%s.%s", IPchecker, IPchecker, IPchecker, IPchecker);
}
