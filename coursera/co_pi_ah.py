import re

def le_assinatura():

    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que  aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)
        
    
def transforma_lista_palavras(texto):
    ''' Cria uma lista de palavras existentes num texto '''

    lista_palavras = []
    
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras = separa_palavras(frase)
            lista_palavras += palavras
            
    return lista_palavras
    
    
def calcula_wal(lista_palavras):
    ''' Tamanho médio de palavra é a somados tamanhos das palavras dividida pelo número total de palavras. '''

    soma_tamanho_palavras = 0
    total_palavras = len(lista_palavras)
    
    for palavra in lista_palavras:
        soma_tamanho_palavras += len(palavra)
        
    return soma_tamanho_palavras / total_palavras

def calcula_ttr(lista_palavras):
    ''' Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 45=0.8 '''
    
    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    total_palavras = len(lista_palavras)
    
    return palavras_diferentes / total_palavras

def calcula_hlr(lista_palavras):
    '''Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 35=0.6'''
    
    total_palavras = len(lista_palavras)
    palavras_unicas = n_palavras_unicas(lista_palavras)
    
    return palavras_unicas / total_palavras
    
def calcula_sal(texto):
    '''Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).'''
    
    sentencas = separa_sentencas(texto)
    total_sentencas = len(sentencas)
    total_caracteres = 0
    
    for sentenca in sentencas:
        total_caracteres += len(sentenca)
    
    return total_caracteres / total_sentencas
    
def calcula_sac(texto):
    '''Complexidade de sentença é o número total de frases divido pelo número de sentenças.'''
    
    sentencas = separa_sentencas(texto)
    frases = []
    
    for sentenca in sentencas:
        frases += separa_frases(sentenca)
    
    total_sentencas = len(sentencas)
    total_frases = len(frases)
    
    return total_frases / total_sentencas
    
def calcula_pal(texto):
    '''Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).'''
    
    sentencas = separa_sentencas(texto)
    total_frases = 0
    total_caracteres = 0
    
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:        
            total_caracteres += len(frase)
            total_frases += 1
    
    return total_caracteres / total_frases

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    lista_palavras = transforma_lista_palavras(texto)
    
    wal = calcula_wal(lista_palavras)
    ttr = calcula_ttr(lista_palavras)
    hlr = calcula_hlr(lista_palavras)
    sal = calcula_sal(texto)
    sac = calcula_sac(texto)
    pal = calcula_pal(texto)
    
    return [wal, ttr, hlr, sal, sac, pal]
    
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    soma_resultados = 0
    
    for i in range(len(as_a)):
        soma_resultados += abs(as_a[i] - as_b[i])
    
    return soma_resultados / 6
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    menor_grau = 100000
    grau_atual = 0
    n_texto = 0
    co_pi_ah = 0
    
    for texto in textos:
        n_texto += 1
        assinatura = calcula_assinatura(texto)
        grau_atual = compara_assinatura(assinatura, ass_cp)
        
        if grau_atual < menor_grau:
            menor_grau = grau_atual
            co_pi_ah = n_texto
   
    return co_pi_ah
   
def main():
    assinatura_copiah = le_assinatura()
    textos = le_textos()
    
    
    print(avalia_textos(textos, assinatura_copiah))
    

main()
