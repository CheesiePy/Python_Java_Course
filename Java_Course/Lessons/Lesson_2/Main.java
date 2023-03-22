package Lessons.Lesson_2;
public class Main {
    public static void main(String[] args) {
        // Dog dog = new Dog(5, "Rex", "German Shepherd");
        // dog.eat();
        // dog.bark();

        Cat cat1 = new Cat(1, "Alex");
        Animal cat2 = new Cat(3, "Ale");
        Cat cat3 = new Cat(4, "Alexy");
        Cat cat4 = new Cat(6, "Alexis");
        Dog dog = new Dog(15, "Pongo", "Germen shepperd");
        Turtle turtle = new Turtle();

        Animal[] animals_array = {cat1, cat2, cat3, cat4, dog, turtle};

        for(int i = 0; i < animals_array.length; i++){
            System.out.println(animals_array[i]);
        }

        Cat cat = new Animal(1, "obji");

        cat.eat();

        
        

    }
    
}
