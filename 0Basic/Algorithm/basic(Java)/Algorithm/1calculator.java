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
        Scanner scanner2 = new Scanner(System.in);
        Scanner scanner3 = new Scanner(System.in);
        System.out.println(solution.solution(scanner, scanner2, scanner3));
    }
    String solution(Scanner scanner, Scanner scanner2, Scanner scanner3){
        String title = " ### Calculator ### ";
        System.out.println("First number : ");
        int a = scanner.nextInt();
        System.out.println("+, -, *, /, % : ");
        String b = scanner2.next();
        System.out.println("Second number : ");
        int c = scanner.nextInt();
        return title;
    }
}










