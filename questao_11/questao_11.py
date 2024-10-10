# Classes Abstratas Crie uma classe abstrata Funcionario com um método abstrato calcularSalario. Derive classes como FuncionarioHorista e FuncionarioAssalariado que
# implementam calcularSalario de formas distintas.

from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora

class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome, salario_mensal):
        self.nome = nome
        self.salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.salario_mensal

funcionario1 = FuncionarioHorista("Junior", 160, 20)
funcionario2 = FuncionarioAssalariado("Vanessa", 3000)

print(f"Salário de {funcionario1.nome}: R$ {funcionario1.calcular_salario():.2f}")
print(f"Salário de {funcionario2.nome}: R$ {funcionario2.calcular_salario():.2f}")
