package Algorithm;
import java.util.*;

class Solution2{
    public static void main(String[] args) {
        Solution2 solution2 = new Solution2();
        Scanner scanner = new Scanner(System.in);
        System.out.println("First number : ");
        int a = scanner.nextInt();
        System.out.println("+, -, *, /, % : ");
        String b = scanner.next();
        System.out.println("Second number : ");
        int c = scanner.nextInt();
        System.out.println(solution2.solution2(a, b, c));
    }
    String solution2(int a, String b, int c){
        String title = "### Calculator ###";
        int answer = 0;
        if(b.equals("+")){answer = a + c;}
        else if(b.equals("-")){answer = a - c;}
        else if(b.equals("*")){answer = a * c;}
        else if(b.equals("/")){answer = a / c;}
        else if(b.equals("%")){answer = a % c;}
        return title;
    }
}

