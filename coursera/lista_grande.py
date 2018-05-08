from random import randint

def lista_grande(n):
    lista = []
    
    for i in range(n):
        lista.append(randint(-1000,10000))
    
    return lista
