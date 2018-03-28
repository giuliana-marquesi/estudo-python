#Receba um número inteiro na entrada e imprima
#
#FizzBuzz
#
#na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

inteiro = int(input("Qual será o inteiro? "))

if inteiro % 3 == 0 and inteiro % 5 == 0:
    print("FizzBuzz")
else:
    print(inteiro)
