def menor_nome(lista_de_nomes):
    palavra_menor = lista_de_nomes[0].strip()
    for nome in lista_de_nomes:
        if len(nome.strip()) < len(palavra_menor):
            palavra_menor = nome.strip()
    return palavra_menor.capitalize()
    
def testa_mais_curto(nomes, menor):
    if mais_curto(nomes) != menor:
        print("\nLista:", nomes, "\tEsperado:", menor)
    else:
        print("+", end= "")

def mock_mais_curto():
    
    lista_nomes = [
                ["  cristina", "Márcia", " Sandra", "Maria", "vanessa", "   priscila"],
                ["ROBERTA", "Ana     ", "Leticia", "isabela"], 
                ["juliana", "bel", "josefa", "ana"], 
                ["LUCIANA", "mar i anne", "marcela"], 
                ["maroca", "   ana", "marta", "bel"]
                ]
    lista_respostas = ["Maria", "Ana", "Bel", "Luciana", "Ana"]
    
    for i in range(len(lista_nomes)):
        testa_mais_curto(lista_nomes[i], lista_respostas[i])
        
