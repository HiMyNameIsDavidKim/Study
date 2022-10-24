package Algorithm;
import java.util.*;

// Java에서 가장 기본적인 형태의 구조
// class Solution1{
//     public static void main(String[] args) {
//         Solution1 solution1 = new Solution1();
//         System.out.println(solution1.solution());
//     }

//     String solution(){
//             String title = "Hello World!";
//             return title;
//     }
// }

class Solution0{
    public static void main(String[] args) {
        new Solution0().solution();
    }
    
    void solution(){
        int[] arr = createArray();
        arr = sortArray(arr);
        printArray(arr);
    }
    int[] createArray(){
        int[] arr = new int[10];
        for(int i=0;i<arr.length;i++){
            arr[i] = (int)((Math.random()*10)+1);
            for(int j=0;j<i;j++){
                if(arr[j] == arr[i]){i--;}
            }
        }
        return arr;
    }
    int[] sortArray(int[] arr){
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length-1;j++){
                if(arr[j] > arr[j+1]){
                    int t = arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=t;
                }
            }

        }
        return arr;
    }
    void printArray(int[] arr){
        for(int i=0;i<arr.length;i++){
            System.out.println(arr[i]);
        }
    }
}

