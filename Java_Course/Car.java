public class Car {
    // atributes
    int year;
    int foul;

    public Car(int year, int foul){
        this.foul = foul;
        this.year = year;
    }

    public void run(){
        while(coundtion){ // כל עוד יש דלק הרכב ממשיך לנסוע
            System.out.println(this.foul);
            this.foul--;
        }
    }

    
}
