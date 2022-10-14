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

// //버블소트의 기본 개념
// for(int i = 0; i < arr.length; i++){ //가장 작은 수가 올 자리
//     for (int j = arr.length - 1; j > i; j--){ //뒤에서부터 스캔
//         if (arr[j] < arr[j-1]){ //뒤에 수가 작으면 앞으로 계속 옮겨줌
//             int t = arr[j]; 
//             arr[j] = arr[j-1];
//             arr[j-1] = t;
//         }
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
        arr = sortArray(arr);
        printArray(arr);
    }
    int[] createArray(){
        int[] arr = new int[10];
        for(int i = 0; i < arr.length; i++){
            arr[i] = (int)((Math.random()*10)+1); //1~10까지 랜덤
            for(int j = 0; j < i; j++){ //중복제거 하는 방법.
                if(arr[j]==arr[i]){i--;}
            }
        }
        return arr;
    }
    int[] sortArray(int[] arr){ //1~10으로 정렬하자.
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length-1;j++){
                if(arr[j] > arr[j+1]){
                    int t = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = t;
                }
            }
        }
        return arr;
    }
    void printArray(int[] arr){
        System.out.println(Arrays.toString(arr));
        return;
    }
}
