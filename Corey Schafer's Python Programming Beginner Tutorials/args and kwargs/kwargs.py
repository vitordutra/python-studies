def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


minha_funcao(nome="caelum")


dicionario = {"nome": "joao", "idade": 25}
minha_funcao(**dicionario)
