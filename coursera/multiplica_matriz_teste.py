def multiplicacao(matA, matB):
    C = []
    for linha in range(len(matA)):
        C.append([])
        for coluna in range(len(matB[0])):
            C[linha].append(0)
            for k in range(len(matA[0])):
               C[linha][coluna] += matA[linha][k] * matB[k][coluna]
    return C
            

            
            
