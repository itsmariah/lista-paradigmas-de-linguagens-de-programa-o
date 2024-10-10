# Exceções/Erros Personalizados: Crie uma classe de exceção personalizada SaldoInsuficienteException em Java e Python, ou error em Golang,
# que seja lançada quando houver uma tentativa de saque superior ao saldo disponível na classe ContaBancaria

class SaldoInsuficienteException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteException("Saldo insuficiente para realizar o saque.")
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")

conta = ContaBancaria("Natan", 180)

try:
    conta.sacar(250)
except SaldoInsuficienteException as e:
    print(e)
