class Calculadora:
    def somar(self, *args):
        return sum(args)

calc = Calculadora()

resultado1 = calc.somar(10, 20)
resultado2 = calc.somar(10, 20, 30)

print("Resultado da soma de dois números:", resultado1)
print("Resultado da soma de três números:", resultado2)
