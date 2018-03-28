# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

numero = int(input("digite o valor de n: "))
ehAdjacente = False
anterior = -1
digito = 0

while numero > 0 and not ehAdjacente:
    digito = numero % 10

    if digito == anterior:
        ehAdjacente =True

    numero = numero // 10
    anterior = digito

if ehAdjacente:
    print("sim")
else:
    print("não")

