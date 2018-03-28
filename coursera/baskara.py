# calcular as raízes de uma equação quadrática. Quando delta for menor que zero, informar que as
# raízes nao serão valores reais.

import math

a = int(input("Informar o valor de a: "))
b = int(input("Informar o valor de b: "))
c = int(input("Informar o valor de c: "))

delta = b**2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    x1 = (-b + math.sqrt(delta))/ (2 * a)
    x2 = (-b - math.sqrt(delta))/ (2 * a)

    if x1 == x2:
        print("a raiz desta equação é", x1)
    else:
        if x1 < x2:
            print("as raízes da equação são", x1, "e", x2)
        else:
            print("as raízes da equação são", x2, "e", x1)

