#lista que recebe valores até receber 0. Quando encerrada deve imprimir os valores na ordem inversa

lista_inteiros = []
num = int(input("Digite um numero inteiro: "))

while num != 0:
    lista_inteiros.append(num)
    num = int(input("Digite um numero inteiro: "))

for i in range(len(lista_inteiros) - 1, -1, -1):
    print(lista_inteiros[i])

