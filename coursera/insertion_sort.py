def insertion_sort(lista):
    for i in range(1, len(lista)):
        j = i
        while lista[j -1] > lista[j] and j > 0:
            lista[j], lista[j -1] = lista[j -1], lista[j]
            j -= 1
    return lista
