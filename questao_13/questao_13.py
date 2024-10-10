# Métodos Estáticos: Adicione um método estático à classe Matematica que calcula o fatorial de um número. Em Python, utilize @staticmethod, em Java static, 
# e em Golang crie uma função regular na struct.

class Matematica:
    @staticmethod
    def fatorial(n):
        if n < 0:
            raise ValueError("Fatorial não é definido para números negativos.")
        if n == 0 or n == 1:
            return 1
        return n * Matematica.fatorial(n - 1)

numero = 5
resultado = Matematica.fatorial(numero)
print(f"O fatorial de {numero} é {resultado}.")
