import java.io.*;
import java.util.*;
import java.util.Arrays;


public class Solution {

    static boolean isAnagram(String a, String b) {
		
		if (a.length() != b.length()) return(false);
        a = a.toLowerCase();
        b = b.toLowerCase();
        
        char[] charArrayA = a.toCharArray();
        char[] charArrayB = b.toCharArray();

        Arrays.sort(charArrayA);
        Arrays.sort(charArrayB);
		    //System.out.println(Arrays.toString(charArrayA));
		    //System.out.println(Arrays.toString(charArrayB));
	
        for (int i = 0; i < charArrayA.length; i++) {
            if (charArrayA[i] != charArrayB[i]) {
                return false;
            }
        }
        return(true);
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

