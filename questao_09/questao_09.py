from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Relatorio(Imprimivel):
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def imprimir(self):
        print(f"Relatório: {self.conteudo}")

class Contrato(Imprimivel):
    def __init__(self, partes):
        self.partes = partes

    def imprimir(self):
        print(f"Contrato: {self.partes}")

relatorio = Relatorio("Relatório Mensal")
contrato = Contrato("Contrato de Prestação de Serviços")

relatorio.imprimir()
contrato.imprimir()
