def ordenada(lista):
    for i in range(1, len(lista)):
        if lista[i - 1] > lista[i]:
            return False
    return True
    
if __name__ == '__main__':
    
    l1 = [4,7,67,-2,0,5,6,9,10]
    l2 = [-10,45,67,88,100,300,2048,3000]
    l3 = [-10,45,67,88,100,300,2048,300]
    
    assert ordenada(l1) == False
    assert ordenada(l2) == True
    assert ordenada(l3) == False
