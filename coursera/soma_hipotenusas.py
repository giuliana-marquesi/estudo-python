def eh_hipotenusa(n):
    quadrado = n ** 2
    cat_a = 3
    while cat_a < n:
        cat_b = 3
        while cat_b < n:
            if cat_a ** 2 + cat_b ** 2 == quadrado:
                return True
            cat_b = cat_b + 1
        cat_a = cat_a + 1
    return False

def soma_hipotenusas(n):
    soma = 0
    while n >= 5:
        if eh_hipotenusa(n):
            soma = soma + n
        n = n - 1
    return soma

def main():

    x = int(input("numero: "))
    print(soma_hipotenusas(x))

main()
