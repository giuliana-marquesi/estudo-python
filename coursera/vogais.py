#Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
#
#Note que
#
#vogal("a") deve devolver True
#
#vogal("b") deve devolver False
#
#vogal("E") deve devolver True
#
#Os valores True e False devolvidos devem ser do tipo bool (booleanos)
#
#Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.

def vogal(letra):
    vogais = ['a','e','i','o','u','A','E','I','O','U']

    for vogal in vogais:
        if letra == vogal:
            return True
    return False

def test_vogal_a():
    assert vogal('a') == True

def test_vogal_x():
    assert vogal('x') == False

def test_vogal_E():
    assert vogal('E') == True

def test_vogal_J():
    assert vogal('J') == False
