package Lessons.Lesson_2;
public class Animal{
    int age;
    String name;

    public Animal(){
        this.name = "Goerge";
        this.age = 25;
    }

    public Animal(int age, String name) {
        this.age = age;
        this.name = name;
    }

    public void eat() {
        System.out.println("Animal is eating");
    }

    @Override
    public String toString() {
        return this.getClass() + " [age=" + age + ", name=" + name + "]";
    }

}
