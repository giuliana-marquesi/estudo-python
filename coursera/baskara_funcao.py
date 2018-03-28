# calcular as raízes de uma equação quadrática. Quando delta for menor que zero, informar que as
# raízes nao serão valores reais.

import math

def pegaValor(nomeVariavel):
    frase = "Informar o valor de " + nomeVariavel + " : "
    return int(input(frase))

def calculaRaiz(b, raizDelta, a):
    return (-b + raizDelta)/ (2 * a) 

def printaOrdenado(frase, x1, x2):
    if x1 < x2:
        print(frase, x1, x2)
    else:
        print(frase, x2, x1)

def exibeRaizes(b, delta, a):
    raizDelta = math.sqrt(delta)
    x1 = calculaRaiz(b, raizDelta, a)
    x2 = calculaRaiz(b, - raizDelta, a)

    if delta == 0:
        print("a raíz da equação é", calculaRaiz(b, raizDelta, a))
    else:
        printaOrdenado("as raízes da equação são", x1, x2)

a = pegaValor("a")
b = pegaValor("b")
c = pegaValor("c")

delta = b**2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    exibeRaizes(b, delta, a)
