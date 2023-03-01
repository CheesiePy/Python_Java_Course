package Lessons.Lesson_1;
public class Car {
    // atributes - שדות
    int year;
    int foul;
    String model;
    // constractor - בנאי
    public Car(int year, int foul){
        this.foul = foul;
        this.year = year;
        
    }

    // methods...
    public void run(){
        while(this.foul > 0){ // כל עוד יש דלק הרכב ממשיך לנסוע
            System.out.println("foul levels: " + this.foul);
            this.foul--;
        }
    }
}
