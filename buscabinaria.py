lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


def busca_linear(lista, item):
    for i in range(len(lista) - 1):
        if lista[i] == item:
            return i
        else:
            return None


resultado = busca_binaria(lista, 19)
if resultado:
    print(f"O número existe e está na posição:[{resultado}] da sua lista.")
else:
    print("Esse número não existe na lista.")
