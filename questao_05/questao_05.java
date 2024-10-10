import java.util.ArrayList;
import java.util.List;

abstract class Animal {
    public abstract void som();
}

class Cachorro extends Animal {
    @Override
    public void som() {
        System.out.println("O cachorro faz: Au Au!");
    }
}

class Gato extends Animal {
    @Override
    public void som() {
        System.out.println("O gato faz: Meow!");
    }
}

public class questao_05 {
    public static void fazerSom(List<Animal> animais) {
        for (Animal animal : animais) {
            animal.som();
        }
    }

    public static void main(String[] args) {
        List<Animal> animais = new ArrayList<>();
        animais.add(new Cachorro());
        animais.add(new Gato());

        fazerSom(animais);
    }
}
