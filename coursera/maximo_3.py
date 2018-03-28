#Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.
#
#Note que
#
#maximo(30,14,10) deve devolver 30
#
#maximo(0,-1, 1) deve devolver 1

def maximo(x, y, z):
    maximo = x
    if maximo < y:
        maximo = y
    if maximo < z:
        maximo = z
    return maximo

def test_maximo_301410():
    assert maximo(30, 14, 10) == 30

def test_maximo_0menos1e1():
    assert maximo(0, -1, 1) == 1

def test_maximo_239082():
    assert maximo(23, 90, 82) == 90

def test_maximo_numerosnegativos():
    assert maximo(-20, -10, -3) == -3


