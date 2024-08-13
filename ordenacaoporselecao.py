def busca_menor(array):
    menor = array[0]
    menor_indice = 0
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_selecao(array):
    novo_array = []
    for i in range(len(array)):
        menor = busca_menor(array)
        novo_array.append(array.pop(menor))
    return novo_array


array_sem_ordem = [5, 3, 6, 2, 1, 10]
print(ordenacao_por_selecao(array_sem_ordem))
