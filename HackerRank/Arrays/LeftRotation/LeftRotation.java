import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class LeftRotation {

    public static int[] arrayLeftRotation(int[] data, int numOf, int rotateBy) {
      int toShift = rotateBy%numOf;
      int[] front = Arrays.copyOfRange(data,0,toShift);
      int[] end = Arrays.copyOfRange(data,toShift,data.length);
      //System.out.println(Arrays.toString(front));
      //System.out.println(Arrays.toString(end));
      int[] out = new int[numOf];
      System.arraycopy(end, 0, out, 0, end.length);
      System.arraycopy(front, 0, out, end.length, front.length);
      
      return out;
        
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
      
        int[] output = new int[n];
        output = arrayLeftRotation(a, n, k);
        for(int i = 0; i < n; i++)
            System.out.print(output[i] + " ");
      
        System.out.println();
      
    }
}