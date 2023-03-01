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

        Animal[] cat_array = {cat1, cat2, cat3, cat4, dog};

        for(int i = 0; i < cat_array.length; i++){
            cat_array[i].eat();
        }
        Turtle turtle = new Turtle();

        System.out.println(turtle.name);

    }
    
}
