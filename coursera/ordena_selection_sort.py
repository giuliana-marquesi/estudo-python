def ordena(lista):
    for i in range(len(lista) - 1):
        pos_menor_elemento = i
        
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[pos_menor_elemento]:
                pos_menor_elemento = j
                
        lista[i], lista[pos_menor_elemento] = lista[pos_menor_elemento] , lista[i]
    
    return lista
