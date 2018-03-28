def insertion(lista):
    for i in range(1, len(lista)):
        j = i
        while lista[j] < lista[j -1] and j > 0:
            lista[j], lista[j - 1] = lista[j -1], lista[j]
            j -= 1

    return lista

if __name__ == '__main__':
    l1 = [3, 5, 6, 0, 2, 4, 9,8,7,1]
    insertion(l1)
    print(l1)
