#Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:
#
#    Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida;
#    Caso contrário, o computador toma a inciativa de começar o jogo.
#
#Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.
#
#Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora
#
#Campeonatos
#
#Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o melhor jogador. Assim, uma vez que a função partida esteja funcionando, você deverá criar uma outra função chamada campeonato. Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato. O placar deve ser impresso na forma
#
#O programa deve implementar:
#
#    Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima jogada do computador de acordo com a estratégia vencedora.
#    Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.
#    Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.
#
#Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no tabuleiro e qual é o máximo de peças a retirar em cada jogada.
#
#Cuigdado: o corretor automático não funciona bem se você tiver alguma chamada a input() antes da definição de todas as funções do jogo (a menos que essa chamada esteja dentro de uma função). Se seu programa usar input() sem que ele esteja dentro de alguma função, coloque-o no final do programa.

def intro():
    escolha = 0
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print(" ")
    print("1 - Para jogar uma partida isolada")
    escolha = int(input("2 - Para jogar um campeonato "))
    print("")
    return escolha

def computador_escolhe_jogada(n, m):
    pecas_tirar = 1
    eme_mais_um = m + 1
    while pecas_tirar <= m:
        if eme_mais_um * pecas_tirar == n or n - pecas_tirar == 0:
            return pecas_tirar
        pecas_tirar = pecas_tirar + 1
    return m

def usuario_escolhe_jogada(n,m):
    pecas_tirar = int(input("Quantas peças você vai tirar? "))
    while pecas_tirar > n or pecas_tirar > m:
        print("")
        print("Oops! Jogada inválida! Tente novamente!")
        print("")
        pecas_tirar = int(input("Quantas peças você vai tirar? "))
    return pecas_tirar

def quem_comeca(n,m):
    if n % (m+1) == 0:
        print("Você começa!")
        jogador = 0
    else:
        print("Computador começa!")
        jogador = 1

    print("")
    return jogador

def exibe_ganhador_partida(jogador):
    if jogador == 0:
        print("Fim de jogo! Computador ganhou!")
        print("")
    else:
        print("Fim de jogo! Você ganhou!")
        print("")

def partida():
    n = 0
    m = 0
    while n <= 0 or m >= n:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        print("")

    escolha = 0
    jogador = quem_comeca(n,m)

    while n > 0:
        jogador = (jogador + 1) % 2
        if jogador == 0:
            escolha = computador_escolhe_jogada(n,m)
            print("Computador tirou", escolha, "peças.")
        else:
            escolha = usuario_escolhe_jogada(n, m)
            print("Você tirou", escolha, "pecas.")
        n = n - escolha

        if n > 0:    
            print("Agora restam" , n , "peças no tabuleiro.")
            print("")

    exibe_ganhador_partida(jogador)
    return jogador

def campeonato():
    rodada = 1
    voce = 0
    computador = 0
    print("Você escolheu um campeonato!")
    print("")

    while rodada <= 3:
        print("**** Rodada", rodada, "****")
        print("")
        resultado = partida()
        if resultado == 0:
            computador = computador + 1
        else:
            voce = voce + 1
        rodada = rodada + 1
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você", voce, "X", computador, "Computador")

escolha = 0
while escolha < 1 or escolha > 2:
    escolha = intro()
if escolha == 1:
    partida()
else:
    campeonato()

