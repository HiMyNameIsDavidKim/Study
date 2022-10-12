package Algorithm.Greedy;
import java.util.*;;

class Change {
    public static void main(String[] args) {
        Change change = new Change();
        System.out.println(change.solution());
    }

    String solution(){
        String title = "### Business Travel Expense ###";
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please input name : ");
        String name = scanner.next();
        System.out.println("Please input money : ");
        int money = scanner.nextInt();
        int mok = 0;
        int nmg = 0;
        String result = "";
        int[]unit = {50000, 10000, 5000, 1000, 500, 100, 50, 10}; //자바의 리스트 선언법
        for(int i = 0; i < unit.length; i++){ //인덱스로만 사용될 때 시절의 i 사용법.
            mok = money / unit[i];
            nmg = money % unit[i];
            money = nmg;
            result += mok+"\t";
        
        }
        return String.format(
        "%s\n"+
        "******************************************************\n"+
        "이름 출장비 오만원 만원 오천원 천원 오백원 백원 오십원 십원 오원 일원\n"+
        "******************************************************\n"+
        "%s %d %s\n"+
        "******************************************************\n",
        title, name, money, result);
    }
}
