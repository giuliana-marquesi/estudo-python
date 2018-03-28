#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
#
#Note que
#
#maior_primo(100) deve devolver 97
#
#maior_primo(7) deve devolver 7
#
#Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o número é primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.

def ehPrimo(k):
    n = 2
    while n < k:
        if k % n == 0:
            return False
        n = n + 1
        print(n)
    return True

def maior_primo(n):
    while not ehPrimo(n):
        n = n - 1
    return n

def test_maior_primo100():
    assert maior_primo(100) == 97

def test_maior_primo7():
    assert maior_primo(7) == 7

def test_maior_primo6():
    assert maior_primo(2) == 2

def test_ehPrimo2():
    assert ehPrimo(2) == True 

def test_ehPrimo7():
    assert ehPrimo(7) == True

def test_ehPrimo161():
    assert ehPrimo(161) == False

def test_ehPrimo113():
    assert ehPrimo(113) == True
