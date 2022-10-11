package Algorithm;
import java.util.*;

class SolutionBMI {
    public static void main(String[] args) {
        SolutionBMI solution = new SolutionBMI();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please input your name : ");
        String name = scanner.next();
        System.out.println("Please input your height(m) : ");
        Float m = scanner.nextFloat();
        System.out.println("Please input your weight(kg) : ");
        int kg = scanner.nextInt();
        System.out.println(solution.solution(name, m, kg));
    }

    String solution(String name, Float m, int kg){
        String title = "### Body Mass Index ###";
        Float bmi = (kg) / (m * m);
        String index = "";
        if(bmi >= 35){index = "고도 비만";}
        else if(bmi >= 30){index = "중도 비만";}
        else if(bmi >= 25){index = "경도 비만";}
        else if(bmi >= 23){index = "과체중";}
        else if(bmi >= 18.5){index = "정상";}
        else if(bmi < 18.5){index = "저체중";}

        return String.format(
            "%s\n"+
            "***************************\n"+
            "이름 키(cm) 몸무게(kg) 비만도\n"+
            "***************************\n"+
            "%s %.0f %d %s\n"+
            "***************************"
            ,title, name, m*100, kg, index);
    }
}
