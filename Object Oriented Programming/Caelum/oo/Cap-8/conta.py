import datetime


class Historico:
    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []

    def imprime(self):
        print("data de abertura: {}".format(self._data_abertura))
        print("Transações: ")
        for t in self._transacoes:
            print("-", t)


class Cliente:
    # Existe cliente sem conta, mas não existe conta sem cliente
    def __init__(self, nome, sobrenome, cpf):
        """
        nome -> str
        sobrenome -> str
        cpf -> str
        """
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        """
        numero -> str
        titular -> Cliente

        **Relacionamento de agregação: Cliente é uma classe que existe
        independentemente de Conta**
        Classe Conta *tem um* cliente

        saldo -> float
        limite -> float
        """
        self.numero = numero
        self.titular = titular  # instância da classe cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico._transacoes.append("depósito de {}".format(valor))

    def saca(self, valor):
        if self.saldo < valor:
            return False

        self.saldo -= valor
        self.historico._transacoes.append("saque de {}".format(valor))
        return True

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        print(
            f"Dados do cliente: {self.titular.nome} {self.titular.sobrenome}, CPF: {self.titular.cpf}"
        )
        self.historico._transacoes.append(
            "tirou extrato - saldo de {}".format(self.saldo)
        )

    def transfere_para(self, destino, valor):
        """ destino: parâmetro do tipo Conta """
        retirou = self.saca(valor)
        if not retirou:
            return False

        destino.deposita(valor)
        self.historico._transacoes.append(
            "Transferência de {} para conta {}".format(valor, destino.numero)
        )
        return True
