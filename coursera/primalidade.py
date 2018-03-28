# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

numero = int(input("digite n: "))
ehPrimo = True
i = 2

while i < numero and ehPrimo:
    if numero % i == 0:
        ehPrimo = False
    i = i + 1

if ehPrimo:
    print("primo")
else:
    print("não primo")
