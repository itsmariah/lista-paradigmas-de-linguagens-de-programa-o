# 3) Encapsulamento: Implemente uma classe "ContaBancaria" com atributos saldo, titular e métodos depositar e sacar. Use encapsulamento para proteger o atributo saldo.

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso!")
        elif valor > self.__saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        print(f"Saldo atual de {self.__titular}: R${self.__saldo}")

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("O saldo não pode ser negativo.")

conta1 = ContaBancaria("Arthur", 500)

conta1.exibir_saldo()
conta1.depositar(200)
conta1.exibir_saldo()

conta1.sacar(150)
conta1.exibir_saldo()

conta1.sacar(1000)
