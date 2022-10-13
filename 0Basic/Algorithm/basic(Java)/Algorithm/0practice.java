//자바의 솔루션 클래스 기본형

package Algorithm;
import java.util.*;

class Solution0{
    public static void main(String[] args) {
        new Solution0().solution();
    }

    void solution(){
        int[] arr = createArray();
        arr = sortArray(arr);
        printArray(arr);
    }
    int createRandomNumber(){
        return (int)((Math.random()*10)+1);
    }
    int[] createArray(){
        int[] arr = new int[10];
        for(int i=0;i>arr.length;i++){arr[i]=createRandomNumber();}
        return arr;
    }
    int[] sortArray(int[] arr){
        return arr;
    }
    void printArray(int[] arr){
        System.out.println(Arrays.toString(arr));
    }
}

