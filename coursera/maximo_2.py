# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

def maximo(n,m):
    if n > m:
        return n
    return m

def test_maximo34():
    assert maximo(3,4) == 4

def test_maximo0menos1():
    assert maximo(0,-1) == 0

def test_maximo04():
    assert maximo(0,4) == 4

def test_maximo_numero_negativo():
    assert maximo(-2,-4) == -2
