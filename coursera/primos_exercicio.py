#Escreva a função n_primos que recebe um número inteiro maior ou igual a 2 como #parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

def n_primos(n):
    qtdade = 1
    while n > 2:
        if ehPrimo(n):
            qtdade = qtdade + 1
        n = n - 1
    return qtdade

def ehPrimo(n):
    aux = 2
    while aux <= n/2:
        if n % aux == 0:
            return False
        aux = aux + 1
    return True

def main():

    num = int(input("Digite um numero maior ou igual a dois: "))
    print(n_primos(num))

main()
