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

public class questao_03 {
    public static void main(String[] args) {
        Animal meuCachorro = new Cachorro();
        Animal meuGato = new Gato();

        meuCachorro.som();
        meuGato.som();
    }
}
