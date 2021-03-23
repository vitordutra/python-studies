def test(arg, *args):
    print("primeiro argumento normal: {}".format(arg))

    for arg in args:
        print("outro argumento: {}".format(arg))


test("python", "é", "muito", "legal")

lista = ["é", "muito", "daora"]

tupla = ("é", "muito", "usado", "em", "AI")

test("python", *lista)
test("python", *tupla)
