def soma_matrizes(m1, m2):

    matriz_somada = []
    
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    
    for i in range(len(m1)):
        linha = []
        
        for j in range(len(m1[0])):
            linha.append(m1[i][j] + m2[i][j])
            
        matriz_somada.append(linha)
        
    return matriz_somada
