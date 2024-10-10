# Agregação: Modele uma classe "Empresa" que agregue uma lista de objetos "Empregado". Cada empregado deve ter atributos como nome, cargo, e salario.

class Empregado:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_detalhes(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}")


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []

    def adicionar_empregado(self, empregado):
        self.empregados.append(empregado)

    def listar_empregados(self):
        print(f"Empregados da empresa {self.nome}:")
        for empregado in self.empregados:
            empregado.exibir_detalhes()


empregado1 = Empregado("Isadora", "Desenvolvedora", 5000)
empregado2 = Empregado("Diogo", "Gerente", 8000)
empregado3 = Empregado("Carolina", "Analista", 6000)

empresa = Empresa("Tech.Dev")
empresa.adicionar_empregado(empregado1)
empresa.adicionar_empregado(empregado2)
empresa.adicionar_empregado(empregado3)

empresa.listar_empregados()
