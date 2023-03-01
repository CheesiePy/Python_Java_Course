public class Dog extends Animal {

    String breed;

    public Dog(int age, String name, String breed) {
        super(age, name);
        this.breed = breed;
    }
    
    public void eat() {
        System.out.println("Dog is eating");
    }
    
    public void bark() {
        System.out.println("Dog is barking");
    }

    @Override
    public String toString() {
        return "Dog [age=" + age + ", name=" + name + ", breed=" + breed + "]";
    }
}
