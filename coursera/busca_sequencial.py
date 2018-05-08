def busca(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False
    
if __name__ == '__main__':
    
    assert busca(['a','e','i'], 'e') == 1
    assert busca([12,13,14],15) == False
