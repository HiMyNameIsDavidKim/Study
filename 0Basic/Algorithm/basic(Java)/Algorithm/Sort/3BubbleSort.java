/**
간소화 버전 숙지
package Algorithm.Sort;

class BubbleSort{
    public static void main(String[] args) {
        new BubbleSort().solution();
    }

    void solution(){
        System.out.println("### Bubble Sort ###");
    }
}
*/
//내림차순 정렬 할때 그 정렬임.



package Algorithm.Sort;
import java.util.*;;

class BubbleSort{
    public static void main(String[] args) {
        new BubbleSort().solution();
    }

    void solution(){
        int randNumber = (int)(Math.random()*10)+1; //1~10까지 랜덤
        System.out.println("Random Number : "+randNumber);
    }

}

