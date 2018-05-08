def confere_numero(primo):
    n = 2
    while n < primo:
        if primo % n == 0:
            return False
        else:
            print("n", n)

            n = n + 1
    return True


x = int(input("um numero: "))

resultado = confere_numero(x)
print(resultado)

