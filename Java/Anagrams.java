import java.util.Scanner;

public class Anagrams {
    
    static boolean isAnagram(String a, String b) {
        char stringA[] = a.toLowerCase().toCharArray();
        char stringB[] = b.toLowerCase().toCharArray();
        if(a.length() != b.length()){
            return false;
        }else{
            java.util.Arrays.sort(stringA);
            java.util.Arrays.sort(stringB);
            return java.util.Arrays.equals(stringA, stringB);
        }
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}