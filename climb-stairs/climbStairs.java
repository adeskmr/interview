import java.util.*; 
import java.lang.*; 

public class climbStairs {
    public static void main(String[] args) {
        int y = 9;
        System.out.println(climbStairs(y));
    }

    public static int climbStairs(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        int case1 = 1;
        int case2 = 1;
        
        for(int i = 2; i <= n; i++){
            int temp = case2;
            case2 = temp+case1;
            case1 = temp;
        }
        return case2;
    }
}