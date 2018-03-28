#Receba um número inteiro na entrada e imprima
#
#Fizz
#
#se o número for divisível por 3. Caso contrário, imprima o mesmo 
#número que foi dado na entrada.

inteiro = int(input("qual será o número inteiro? "))

if inteiro % 3 == 0:
    print("Fizz")
else:
    print(inteiro)
