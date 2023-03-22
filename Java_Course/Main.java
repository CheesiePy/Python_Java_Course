import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String user_input = "";
        int token = 0;
        while (!user_input.equals("quit")){
            System.out.print("Please Enter a number: ");
            user_input = sc.nextLine();
            System.out.println(user_input);    
        }
        
    }
    
}
