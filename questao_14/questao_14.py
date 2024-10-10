#Singleton: Implemente o padrão de projeto Singleton para garantir que apenas uma instância de uma classe Configuracao seja criada.

class Configuracao:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuracao, cls).__new__(cls)
            cls._instance.configuracoes = {}
        return cls._instance

    def set_config(self, chave, valor):
        self.configuracoes[chave] = valor

    def get_config(self, chave):
        return self.configuracoes.get(chave, None)

config1 = Configuracao()
config1.set_config("tema", "escuro")

config2 = Configuracao()
print(config2.get_config("tema"))

print(config1 is config2)
