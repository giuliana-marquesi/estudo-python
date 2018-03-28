# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

n = int(input("Qual é o valor de n? "))
i = 0
impar = 1

while i < n:
    print(impar)
    impar = impar + 2
    i = i + 1
