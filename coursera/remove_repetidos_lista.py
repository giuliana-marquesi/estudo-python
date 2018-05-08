def remove_repetidos(inteiros_repetidos):
    inteiros_unicos = []    
    for num in inteiros_repetidos:
        if not num in inteiros_unicos:
            inteiros_unicos.append(num)
    inteiros_unicos.sort()
    return inteiros_unicos

