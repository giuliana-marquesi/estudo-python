def inicio():
    print ("Bem-vindo ao jogo do NIM! Escolha:")
    print ("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))

    if escolha == 1:
        print ("\nVoce escolheu uma partida isolada!\n")
        partida()
    elif escolha == 2:
        print("\nVoce escolheu um campeonato!")
        campeonato()
    else:
        print("\nVoce fez uma escolha inválida!\n")
        inicio()

def campeonato():
    computador = 0
    usuario = 0
    rodada = 1
    while rodada <= 3:
        print("\n**** Rodada", rodada, "****\n")
        resultado = partida()
        rodada = rodada + 1
        if resultado == 0:
            computador = computador + 1
        else:
            usuario = usuario + 1
    print("**** Final do campeonato! ****\n\nPlacar: Você", usuario, "X", computador, "Computador")

def partida():

    n = 0
    m = 1

    while n < m or n < 1:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

    if n % (m+1) == 0:
        print("\nVoce começa!\n")
        z = usuario_escolhe_jogada(n,m)
        print("Você tirou", z, "peças")
        prox_rodada = 0
    else:
        print("\nComputador começa!\n")
        z = computador_escolhe_jogada(n,m)
        print("\nO computador tirou", z, "peças")
        prox_rodada = 1

    n = n - z

    while n > 0:
        print("Agora restam", n, "peças no tabuleiro\n")        

        if prox_rodada == 0:
            z = computador_escolhe_jogada(n,m)
            print("O computador tirou", z, "peças")             
            prox_rodada = 1
        else:
            z = usuario_escolhe_jogada(n,m)
            print("\nVocê tirou", z, "peças")
            prox_rodada = 0
        
        n = n - z
    
    if prox_rodada == 0:
        print("Fim do jogo! Você ganhou!\n")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!\n")
        return 0

def usuario_escolhe_jogada(n,m):
    y = int(input("Quantas peças você vai tirar? "))

    if y > m or y > n or y <= 0:
        print("\nOops! Jogada inválida! Tente de novo.")
        y = usuario_escolhe_jogada(n,m)
    return y

def computador_escolhe_jogada(n,m):
    z = 1
    while (n - z) % (m+1) != 0 and z < m:
        z = z +1
    return z

inicio()
