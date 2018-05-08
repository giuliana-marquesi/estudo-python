def bubble_sort(lista):
    for i in range(len(lista) - 1, 0, -1):
        estaOrdenado = True
        for j in range(i):
            if lista[j] > lista[j +1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
                estaOrdenado = False
        if estaOrdenado:
            return lista
    return lista
            
