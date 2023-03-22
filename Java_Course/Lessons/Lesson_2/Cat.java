package Lessons.Lesson_2;
public class Cat extends Animal{
    int lifes;

    public Cat(int age, String name){
        super(age, name);
        this.lifes = 9;
    }

    @Override
    public void eat(){
        System.out.println("Cat is eating");
    }
}
