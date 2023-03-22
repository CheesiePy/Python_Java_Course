package Lessons.Lesson_3;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);
        // String user_input = "";
        // int token = 0;
        // while (!user_input.equals("quit")){
        //     System.out.print("Please Enter a number: ");
        //     user_input = sc.nextLine();
        //     System.out.println(user_input);    
        // }
        Task t = new Task();
        t.task1(5, "JavaIsTheBest!");
        System.out.println(t.task2(1994));
        int sum =  t.task4(50000000);
        int sumbad = t.task4_bad(50000000);
        System.out.println("good algo: " + sum);
        System.out.println("normal algo: " + sumbad);

        String rev = t.task5("רק פושטק עלוב בלוע קטשופ קר");
        System.out.println(rev);

    }
    
}
