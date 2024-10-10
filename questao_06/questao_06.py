# Composição Implemente uma classe "Motor" e associe-a a uma classe "Carro". A classe "Carro" deve ter um objeto do tipo Motor como um de seus atributos.

class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"Motor {self.tipo} ligado com {self.potencia} cavalos de potência.")
        else:
            print(f"Motor {self.tipo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"Motor {self.tipo} desligado.")
        else:
            print(f"Motor {self.tipo} já está desligado.")

    def exibir_detalhes(self):
        print(f"Tipo do motor: {self.tipo}, Potência: {self.potencia} cavalos de potência")


class Carro:
    def __init__(self, marca, modelo, ano, motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor

    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}")
        self.motor.exibir_detalhes()

    def ligar_carro(self):
        print(f"Ligando o carro {self.marca} {self.modelo}...")
        self.motor.ligar()

    def desligar_carro(self):
        print(f"Desligando o carro {self.marca} {self.modelo}...")
        self.motor.desligar()


motor_v8 = Motor("V8", 630)  
carro_esportivo = Carro("Audi", "Audi RS6", 2024, motor_v8)

carro_esportivo.exibir_detalhes()

carro_esportivo.ligar_carro()
carro_esportivo.desligar_carro()
