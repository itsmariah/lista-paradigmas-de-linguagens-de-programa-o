# Sobrecarga de Operadores (Python) / Métodos de Conveniência (Java, Go) Em Python, sobrecarregue o operador + para somar dois objetos Produto baseados no preço. 

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __add__(self, other):
        if isinstance(other, Produto):
            return Produto(f"{self.nome} & {other.nome}", self.preco + other.preco)
        return NotImplemented

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}"


produto1 = Produto("Produto A", 50.00)
produto2 = Produto("Produto B", 30.00)


produto_total = produto1 + produto2

print(produto_total)
