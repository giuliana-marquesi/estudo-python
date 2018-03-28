#Receba 4 números inteiros na entrada. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
#
#Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
#
#longe
#
#na saída. Caso o contrário, quando a distância for menor que 10, imprima
#
#perto
import math

xA = int(input("Informe o x do ponto A: "))
yA = int(input("Informe o y do ponto A: "))
xB = int(input("Informe o x do ponto B: "))
yB = int(input("Informe o y do ponto B: "))

diferencaX = (xB - xA) ** 2
diferencaY = (yB - yA) ** 2

distancia = math.sqrt((diferencaX + diferencaY))

if distancia >= 10:
    print("longe")
else:
    print("perto")


