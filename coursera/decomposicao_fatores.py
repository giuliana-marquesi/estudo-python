def main():
    num = int(input("Digite um numero: "))
    primo = 2
    multiplicidade = 0
    
    while num > 1:
        while num % primo == 0:
            num = num // primo
            multiplicidade = multiplicidade + 1
        if multiplicidade > 0:
            print("Fator", primo, "multiplicidade", multiplicidade)        
        primo = primo + 1
        multiplicidade = 0
        

def proximo_primo(primo):
    primo = primo + 1

    while not confere_numero(primo):
        primo = primo + 1
    
    return primo

def confere_numero(primo):
    n = 2
    while n < primo:
        if primo % n == 0:
            return False
        else:
            n = n + 1
    return True
  
main()
