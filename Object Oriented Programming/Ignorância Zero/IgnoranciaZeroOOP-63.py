class ObjetoGrafico:
    def __init__(self, cor):
        self.cor = cor

    # Métodos abstratos
    # O que é abstrair? É simplesmente não escrever nada
    # Esperar que as subclasses dessa classe implementar o que foi abstraído
    # Acontece muito com projetos de programação em equipe
    # Você cria uma classe abstrata e você implementa uma classe e outro colega
    # da equipe implementa outra classe: Ex: superclasse Sprite: subclasse Player e Enemy

    def area(self):
        pass

    def perimetro(self):
        pass

 def info(self):
        print(f"{self.area()} m² serão preenchidos com a cor {self.cor}")

class Banco:
    total = 10000
    reserva = 0.1*total

class Conta:
    total = 10000
    reserva = 0.1

    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= self.valor
