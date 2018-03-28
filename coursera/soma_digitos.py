# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

numero = int(input("Digite o valor de n: "))
soma = 0

while numero > 0:
    soma = soma + (numero % 10)
    numero = numero // 10

print(soma)
