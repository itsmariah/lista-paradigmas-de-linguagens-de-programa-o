# Herança: Crie uma classe base "Animal" com métodos como som. Derive classes como Cachorro e Gato que implementam o método som de maneiras diferentes.

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses")

class Cachorro(Animal):
    def som(self):
        return f"{self.nome} faz: Au Au!"

class Gato(Animal):
    def som(self):
        return f"{self.nome} faz: Miau!"

cachorro = Cachorro("Angel")
gato = Gato("Sushi")

print(cachorro.som())
print(gato.som())
