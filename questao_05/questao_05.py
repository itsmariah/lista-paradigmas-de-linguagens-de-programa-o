# Polimorfismo: Utilize polimorfismo para criar uma função que receba uma lista de objetos "Animal" e chame o método som de cada um, demonstrando comportamento diferente para cada subclasse.

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
        return f"{self.nome} faz: Meow!"

class Passaro(Animal):
    def som(self):
        return f"{self.nome} faz: Piu Piu!"

def emitir_sons(animais):
    for animal in animais:
        print(animal.som())

animais = [
    Cachorro("Angel"),
    Gato("Sushi"),
    Passaro("Ximi")
]

emitir_sons(animais)
