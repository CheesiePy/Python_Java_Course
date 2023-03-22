package Lessons.Lesson_3;
class Task{

    public void task1(int n, String name){
        for(int i = 0 ; i < n; i++){
            System.out.println(name);
        }
    }

    public int task2(int n){
        if (n%2 == 0){
            return n + 2;
        }
        return n + 1;
    }

    public boolean task3(int n){
        // return true if n is even, or flase otherwise
        if(n%2 == 0){
            return true;
        }
        else{
            return false;
        }
    }


    // Method 4
    public int task4(int n){
        // calculate and return the sum of all numbers from 1 to n
        return (1 + n)*n/2;
    }

    public int task4_bad(int n){
        // calculate and return the sum of all numbers from 1 to n
        int sum = 0;
        for(int i = 1; i <= n; i++){
            sum += i;
        }
        return sum;
    }

    // Method 5
    public String task5(String str){
        // reverse the order of characters in a string and return it
        String reverce = "";
        for(int i = 0; i < str.length(); i++){
            reverce += str.charAt(str.length() - 1 - i);
        }
        return reverce;
    }

    // Method 6
    public int task6(int[] arr){
        // find and return the largest integer in an array

        return 0;
    }

    // Method 7
    public boolean task7(String str){
        // check if a string is a palindrome and return true or false
        // רק פושטק עלוב בלוע קטשופ קר V
        // אמא אבא V
        // dad mom V
        // רגע = > עגר X
        return false;
    }

    // Method 8
    public int task8(int n){
        // calculate and return the factorial of a given
        return 0;
    }


}