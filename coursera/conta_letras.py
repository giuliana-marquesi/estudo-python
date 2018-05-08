def conta_letras(frase, contar="vogais"):
    assert contar.lower() == 'vogais' or contar.lower() == 'consoantes'
    
    vogais, consoantes = 0, 0
    
    for letra in frase:
        letraMin = letra.lower()
        if letraMin == 'a' or letraMin == 'e' or letraMin == 'i' or letraMin == 'o' or letraMin == 'u':
            vogais += 1
        elif ord(letraMin) > 96 and ord(letraMin) < 123:
            consoantes += 1
    
    if contar.lower() == 'vogais':
        return vogais
    return consoantes    
