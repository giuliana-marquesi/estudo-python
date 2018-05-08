#retangulo
# Escreva um programa que recebe como entradas (utilize a função input) dois números #inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O #programa deve imprimir uma cadeia de caracteres que represente o retângulo informado #com caracteres '#' na saída.

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

y = 0

while y < altura:
    x = 1
    print("#", end = "")
    while x < largura - 1:
        if y == 0 or y == altura - 1: 
            print("#", end = "")
        else:
            print(" ", end = "")
        x = x + 1
    print("#")
    y = y + 1
