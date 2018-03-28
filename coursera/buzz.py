#Receba um número inteiro na entrada e imprima
#
#Buzz
#
#se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

inteiro = int(input("Qual será o numero inteiro? "))

if inteiro % 5 == 0:
    print("Buzz")
else:
    print(inteiro)
