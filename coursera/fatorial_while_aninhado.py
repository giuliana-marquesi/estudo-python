#receber um sequencia de numeros do usuario. e para cada numero que ele digite 

def main():
    numero = 0

    print("Benvinda ao cálculo de fatorial!\n Digite um numero para calcular fatorial.\nPara sair digite -1")

    while numero != -1:
        numero = int(input("Número: "))
        fatorial(numero)

def fatorial(numero):
    fatorial = 1
    while numero > 1:
        fatorial = fatorial * numero
        numero = numero - 1
    print(fatorial)

main()
