package Algorithm;
import java.util.*;

class Solution0{
    public static void main(String[] args) {
        new Solution0().solution();
    }
    void solution(){
        int[] arr = creatArray();
        arr = sortArray(arr);
        printArray(arr);
    }
    int[] creatArray(){
        int[] arr = new int[10];
        for(int i=0; i<arr.length; i++){
            arr[i] = (int)((Math.random()*10)+1);
            for(int j=0; j<i; j++){
                if(arr[j]==arr[i]){i--;}
            }
        }
        return arr;
    }
    int[] sortArray(int[] arr){
        
        return arr;
    }
    void printArray(int[] arr){
        System.out.println(Arrays.toString(arr));
    }
}

