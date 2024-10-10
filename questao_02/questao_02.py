# Métodos: Adicione um método acelerar e frear à classe Carro que altere um atributo velocidade. Crie um método para exibir a velocidade atual.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"{self.modelo} acelerou. Velocidade atual: {self.velocidade} km/h")

    def frear(self, decremento):
        if self.velocidade - decremento >= 0:
            self.velocidade -= decremento
        else:
            self.velocidade = 0
        print(f"{self.modelo} freou. Velocidade atual: {self.velocidade} km/h")

    def exibir_velocidade(self):
        print(f"Velocidade atual do {self.modelo}: {self.velocidade} km/h")


carro1 = Carro("Peugeot", "208", 2021)
carro2 = Carro("Caoa Chery", "Tiggo 7 Pro", 2020)
carro3 = Carro("Jeep", "Renegade", 2019)

carro1.acelerar(50)
carro1.exibir_velocidade()

carro2.acelerar(30)
carro2.frear(10)
carro2.exibir_velocidade()

carro3.acelerar(70)
carro3.frear(80)
carro3.exibir_velocidade()
