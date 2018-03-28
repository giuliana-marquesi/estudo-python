#Receba 3 números inteiros na entrada e imprima
#
#crescente
#
#se eles forem dados em ordem crescente. Caso contrário, imprima
#
#não está em ordem crescente

x = int(input("primeiro: "))
y = int(input("segundo: "))
z = int(input("terceiro: "))

if x < y and y < z:
    print("crescente")
else:
    print("não está em ordem crescente")
