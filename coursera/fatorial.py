

def fatorial(n):
    fatorial = m = 1

    while m <= n:
        fatorial = fatorial * m
        m = m + 1

    return fatorial

def binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))


n = int(input("Qual será o número n? "))
k = int(input("Qual será o numero k? "))

print("O resultado é", binomial(n,k))
