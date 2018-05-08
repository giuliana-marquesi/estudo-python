def busca(lista,x):
    primeiro = 0
    ultimo = len(lista) -1
    
    while primeiro <= ultimo:
        meio = (ultimo + primeiro) // 2
        print(meio)
        if x == lista[meio]:
            return meio
        elif x > lista[meio]:
            primeiro = meio + 1
        else:
            ultimo = meio - 1
    return False 
