def maiusculas(frase):
    letras = ''
    for letra in frase:
        if ord(letra) > 65 and ord(letra) < 91:
            letras += letra
    return letras
