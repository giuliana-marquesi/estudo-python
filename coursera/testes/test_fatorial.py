# Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.
import '../fatorial.py'

def devolve_numero_fatorial_de_x():
    x = 3
    resultado_fatorial = calcula_fatorial(x)
    assert resultado_fatorial == 6
