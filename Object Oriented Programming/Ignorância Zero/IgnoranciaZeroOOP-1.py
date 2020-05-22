# Python Object-Oriented Programming


class MinhaClasse:
    def __init__(self):
        self.nome = "Pedro"
        self.idade = 45
        print("Construtor chamado com sucesso")

    def imprime(self):
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos")


pedro = MinhaClasse()

pedro.imprime()
