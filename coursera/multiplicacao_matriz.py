import sao_multiplicaveis_matrizes

def multiplicacao(matA, matB):
    assert sao_multiplicaveis_matrizes.sao_multiplicaveis(matA,matB)
    
    C = []
    
    for i in range(len(matA)):
        linha = []
        for j in range(len(matA[0])):
            print(matA[i][j], "x", matB[j][i])
    
if __name__ == '__main__':
    A = [[1,2,3],[4,5,6]]
    B = [[7,8],[6,5],[4,3]]
    
    multiplicacao(A,B)
