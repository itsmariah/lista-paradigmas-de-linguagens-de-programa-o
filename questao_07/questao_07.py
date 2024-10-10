# Associação: Crie uma classe "Escola" e uma classe "Professor". A associação deve permitir que uma escola tenha vários professores, e um professor possa lecionar em várias escolas.

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.escolas = []

    def adicionar_escola(self, escola):
        if escola not in self.escolas:
            self.escolas.append(escola)
            escola.adicionar_professor(self)

    def listar_escolas(self):
        print(f"Professor: {self.nome} leciona nas seguintes escolas:")
        for escola in self.escolas:
            print(f"- {escola.nome}")


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)

    def listar_professores(self):
        print(f"Escola: {self.nome} tem os seguintes professores:")
        for professor in self.professores:
            print(f"- {professor.nome}")


escola1 = Escola("Escola Primária")
escola2 = Escola("Escola Secundária")

professor1 = Professor("Ricardo")
professor2 = Professor("Leandro")

professor1.adicionar_escola(escola1)
professor1.adicionar_escola(escola2)

professor2.adicionar_escola(escola1)

professor1.listar_escolas()
professor2.listar_escolas()

escola1.listar_professores()
escola2.listar_professores()
