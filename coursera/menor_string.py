def teste_pontual(meu_string, resposta_esperada):
    resposta = primeiro_lex(meu_string)
    if resposta == resposta_esperada:
        print("+", end =" ")
    else:
        print("X\nresposta obtida:", resposta, "resposta esperada:", resposta_esperada)

def testa_menor_string():
    teste_pontual(["ana", "maria", " José", "Valdemar"], "ana")
    teste_pontual(["Ana", "josefa", "   ana", "Aaron"], "aaron")
    teste_pontual(["marta", "Marisa", "Marmota", "marinete"], "marinete")
    
def primeiro_lex(meu_string):
    menor = meu_string[0].strip()
    
    for palavra in meu_string:
        palavra_strip = palavra.strip()
        if palavra_strip < menor:
            menor = palavra_strip
    
    return menor
