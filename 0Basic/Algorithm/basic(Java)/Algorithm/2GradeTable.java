/**
자바의 장문 주석처리 방법
 */

package Algorithm;
import java.util.*;

class SolutionGT{
    public static void main(String[] args) {
        SolutionGT solution = new SolutionGT();
        Scanner scanner = new Scanner(System.in);
        System.out.println("input Kor Grade : ");
        int Kor = scanner.nextInt();
        System.out.println("input Math Grade : ");
        int Math = scanner.nextInt();
        System.out.println("input Eng Grade : ");
        int Eng = scanner.nextInt();
        System.out.println(solution.solution(Kor, Math, Eng));
    }

    String solution(int Kor, int Math, int Eng){
        String title = "### Grade Table ###";
        int total = Kor + Math + Eng;
        float avg = total/3;
        String grade = "";
        if(avg >= 90){grade = "A";}
        else if(avg >= 80){grade = "B";}
        else if(avg >= 70){grade = "C";}
        else if(avg >= 60){grade = "D";}
        else if(avg >= 50){grade = "E";}
        else if(avg < 50){grade = "F";}
        return String.format(
        "%s\n"
        +"*******************************\n"
        +"Kor Math Eng Total Avg Grade\n"
        +"*******************************\n"
        +"%d %d %d %d %.1f %s\n"
        +"*******************************\n", title, Kor, Math, Eng, total, avg, grade);
    }
}




