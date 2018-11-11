from blackjack import Dealer, Carta, Jogador

def teste_dealer_quantidade_cartas_baralho():
    dealer = Dealer()
    assert dealer.quantidade_cartas_baralho() == 52

def teste_dealer_descartes_inicio_jogo():
    dealer = Dealer()
    dealer.iniciar_jogo()
    assert dealer.quantidade_cartas_baralho() == 45

def teste_dealer_52_cartas_antes_do_inicio_da_rodada():
    dealer = Dealer()
    assert dealer.quantidade_cartas_baralho() == 52

def teste_dealer_52_cartas_antes_do_inicio_de_qualquer_rodada():
    # Quando inicia o jogo, todas as cartas são
    # devolvidas, tendo um total de 52, portanto
    # se o jogo for iniciado duas vezes, o total deve
    # após o inicio deve ser 45 em ambas (-5 de descarte, -2 para o Dealer)
    dealer = Dealer()
    dealer.iniciar_jogo()
    dealer.iniciar_jogo()
    assert dealer.quantidade_cartas_baralho() == 45

def teste_dealer_43_cartas_apos_entregar_as_do_jogador():
    dealer = Dealer()
    jogador = Jogador('teste')
    dealer.iniciar_jogo()    
    jogador.receber_cartas(dealer.entregar_cartas_jogador())
    assert dealer.quantidade_cartas_baralho() == 43

def teste_dealer_43_cartas_apos_entregar_as_do_jogador_em_duas_rodadas():
    dealer = Dealer()
    jogador = Jogador('teste')
    dealer.iniciar_jogo()    
    jogador.receber_cartas(dealer.entregar_cartas_jogador())
    assert dealer.quantidade_cartas_baralho() == 43    

    dealer.receber_cartas_jogador(jogador.entregar_cartas())
    dealer.iniciar_jogo()
    jogador.receber_cartas(dealer.entregar_cartas_jogador())
    assert dealer.quantidade_cartas_baralho() == 43

def teste_somatorio_cartas():
    dealer = Dealer()

    assert dealer.somatorio_cartas([ 
        Carta('9', ''), 
        Carta('A', ''), 
        Carta('A', '') 
    ]) == 21

    assert dealer.somatorio_cartas([ 
        Carta('7', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', '') 
    ]) == 21

    assert dealer.somatorio_cartas([ 
        Carta('7', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', '') 
    ]) == 20

    assert dealer.somatorio_cartas([ 
        Carta('8', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', '') 
    ]) == 21

    assert dealer.somatorio_cartas([ 
        Carta('9', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', ''),
        Carta('A', '')
    ]) == 13

    assert dealer.somatorio_cartas([ 
        Carta('10', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', ''),
        Carta('A', '')
    ]) == 14

    assert dealer.somatorio_cartas([ 
        Carta('J', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('3', '')
    ]) == 15

    assert dealer.somatorio_cartas([ 
        Carta('J', ''), 
        Carta('A', ''), 
        Carta('A', '')
    ]) == 12

    assert dealer.somatorio_cartas([ 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', ''),
        Carta('A', '')
    ]) == 14

    assert dealer.somatorio_cartas([ 
        Carta('2', ''), 
        Carta('5', ''), 
        Carta('9', ''),
        Carta('A', '')
    ]) == 17

    assert dealer.somatorio_cartas([ 
        Carta('2', ''), 
        Carta('6', ''), 
        Carta('9', ''),
        Carta('4', '')
    ]) == 21

    assert dealer.somatorio_cartas([ 
        Carta('A', ''), 
        Carta('A', '')
    ]) == 12

    assert dealer.somatorio_cartas([ 
        Carta('A', ''),
        Carta('A', ''),
        Carta('J', '')
    ]) == 12

    assert dealer.somatorio_cartas([ 
        Carta('10', ''), 
        Carta('J', ''), 
        Carta('A', ''),
        Carta('A', '')
    ]) == 22

    assert dealer.somatorio_cartas([ 
        Carta('10', ''), 
        Carta('J', ''), 
        Carta('A', ''),
        Carta('A', ''),
        Carta('A', '')
    ]) == 23

    assert dealer.somatorio_cartas([ 
        Carta('10', ''), 
        Carta('J', ''), 
        Carta('2', ''),
        Carta('2', ''),
        Carta('A', '')
    ]) == 25

    assert dealer.somatorio_cartas([ 
        Carta('10', ''), 
        Carta('J', ''), 
        Carta('3', ''),
        Carta('A', '')
    ]) == 24

    assert dealer.somatorio_cartas([ 
        Carta('10', ''), 
        Carta('J', ''), 
        Carta('3', ''),
        Carta('A', ''),
        Carta('A', '')
    ]) == 25

    assert dealer.somatorio_cartas([ 
        Carta('10', ''), 
        Carta('A', ''), 
        Carta('A', ''),
        Carta('J', '')
    ]) == 22

    assert dealer.somatorio_cartas([ 
        Carta('10', ''), 
        Carta('5', ''), 
        Carta('2', ''),
        Carta('3', '')
    ]) == 20

    assert dealer.somatorio_cartas([ 
        Carta('10', ''), 
        Carta('5', ''), 
        Carta('2', ''),
        Carta('3', ''),
        Carta('A', '')
    ]) == 21

    assert dealer.somatorio_cartas([ 
        Carta('10', ''), 
        Carta('Q', ''), 
        Carta('A', '')
    ]) == 21

    assert dealer.somatorio_cartas([ 
        Carta('10', ''), 
        Carta('K', ''), 
        Carta('2', '')
    ]) == 22 

    assert dealer.somatorio_cartas([ 
        Carta('J', ''), 
        Carta('2', '')
    ]) == 12     

def teste_empate():
    dealer = Dealer()
    jogador = Jogador('teste')

    jogador.receber_cartas([Carta('A', ''), Carta('10', '')])
    dealer.receber_cartas([Carta('J', ''), Carta('A', '')])
    assert dealer.resultado_jogador(jogador) == 0

def teste_vitoria_jogador_com_blackjack():
    dealer = Dealer()
    jogador = Jogador('teste')

    jogador.receber_cartas([Carta('10', ''), Carta('A', '')])
    dealer.receber_cartas([Carta('J', ''), Carta('9', '')])
    assert dealer.resultado_jogador(jogador) == 1      

def teste_derrota_jogador_com_soma_maior_que_21():
    dealer = Dealer()
    jogador = Jogador('teste')

    jogador.receber_cartas([Carta('A', ''), Carta('A', ''), Carta('10', ''), Carta('10', '')])
    dealer.receber_cartas([Carta('J', ''), Carta('2', '')])
    assert dealer.resultado_jogador(jogador) == -1

def teste_vitoria_dealer_com_soma_maior_que_jogador():
    dealer = Dealer()
    jogador = Jogador('teste')

    jogador.receber_cartas([Carta('10', ''), Carta('9', '')])
    dealer.receber_cartas([Carta('Q', ''), Carta('J', '')])
    assert dealer.resultado_jogador(jogador) == -1