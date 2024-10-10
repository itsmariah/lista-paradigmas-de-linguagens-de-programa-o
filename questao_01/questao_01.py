# 1) Classes e Objetos Básicos: Crie uma classe "Carro" com atributos como marca, modelo, e ano. Instancie três objetos dessa classe e exiba os detalhes de cada um.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

carro1 = Carro("Peugeot", "208", 2021)
carro2 = Carro("Caoa Chery", "Tiggo 7 Pro", 2020)
carro3 = Carro("Jeep", "Renegade", 2019)

carro1.exibir_detalhes()
carro2.exibir_detalhes()
carro3.exibir_detalhes()
