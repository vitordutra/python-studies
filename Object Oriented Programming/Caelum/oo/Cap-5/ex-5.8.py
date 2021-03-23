def teste_args_kwargs(*args, **kwargs):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)


args = ("um", 2, 3, 4)
teste_args_kwargs(*args)

kwargs = {"arg3": 3, "arg2": "dois", "arg1": "um"}
teste_args_kwargs(**kwargs)


def __init__(self, numero, cliente, saldo, limite):
    # iniciando	outros	parâmetros
    self.historico = Historico()

