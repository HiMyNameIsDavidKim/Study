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


// //소트의 기본 형태.
// package Algorithm.Sort;
// import java.util.*;;

// class BubbleSort{
//     public static void main(String[] args) {
//         new BubbleSort().solution();
//     }

//     void solution(){
//         int[] arr = createArray();
//         int[] arr2 = bubbleSort(arr);
//         print(arr2);
//     }
//     int createRandomNumber(){
//         return (int)(Math.random()*10)+1; //1~10까지 랜덤
//     }
//     int[] createArray(){
//         int[] arr = new int[10];
//         return arr;
//     }
//     int[] bubbleSort(int[] arr){
//         return arr;
//     }
//     void print(int[] arr){
//         return;
//     }
// }



package Algorithm.Sort;
import java.util.*;;

class BubbleSort{
    public static void main(String[] args) {
        new BubbleSort().solution();    
    }

    void solution(){
        int[] arr = createArray();
        int[] arr2 = sortArray(arr);
        printArray(arr2);
    }
    int createRandomNumber(){   
        return (int)((Math.random()*10)+1); //1~10까지 랜덤
    }
    int[] createArray(){
        int[] arr = new int[10];
        for(int i = 0; i < arr.length; i++){
            arr[i] = createRandomNumber();
        }
        return arr;
    }
    int[] sortArray(int[] arr){
        return arr;
    }
    void printArray(int[] arr){
        System.out.println(Arrays.toString(arr));
        return;
    }
}
