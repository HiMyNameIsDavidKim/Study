//클래스 안에서 main치고 엔터치면 자동완성됨.
//sysout 치고 엔터치면 자동완성됨.
//파이썬에서는 메인이 아래에 있었는데 자바에서는 위에 있음.
//파이썬은 생략 버전이고, 자바는 생략 안된 버전임. 비교하면서 보면 똑같음.
package Algorithm;
import java.util.*;

class Solution{
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        System.out.println("First number : ");
        int a = scanner.nextInt();
        System.out.println("+, -, *, /, % : ");
        String b = scanner.next();
        System.out.println("Second number : ");
        int c = scanner.nextInt();
        System.out.println(solution.solution(a, b, c));
    }
    String solution(int a,String b,int c){
        String title = " ### Calculator ### ";
        int answer = 0;
        if(b.equals("+")){answer = a + c;} //==는 숫자 비교만 되고, 스트링 비교는 이렇게 해야함..ㅎㅎ
        else if(b.equals("-")){answer = a - c;}
        else if(b.equals("*")){answer = a * c;}
        else if(b.equals("/")){answer = a / c;}
        else if(b.equals("%")){answer = a % c;}
        else{System.out.println("Wrong input.");}
        return String.format("%s\n%d %s %d = %d", title, a, b, c, answer);
    }
}










