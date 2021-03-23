from conta import Conta, Cliente

cliente1 = Cliente("João", "Gois", "0517390530-10")
cliente2 = Cliente("Jéssica", "Veloso", "063663036-3")
conta = Conta("123-4", cliente1, 120.0, 1000.0)
conta2 = Conta("124-5", cliente2, 200.0, 1000.0)
conta.extrato()
conta2.extrato()

conta.historico.imprime()
conta2.historico.imprime()
