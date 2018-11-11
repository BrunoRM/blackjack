from blackjack import Dealer, Carta, Jogador

def teste_dealer_quantidade_cartas_baralho():
    dealer = Dealer('teste', 'M')
    assert dealer.quantidade_cartas_baralho() == 52

def teste_dealer_descartes_inicio_jogo():
    dealer = Dealer('teste', 'M')
    dealer.iniciar_jogo()
    assert dealer.quantidade_cartas_baralho() == 45

def teste_somatorio_cartas():
    dealer = Dealer('teste', 'M')

    assert dealer.somatorio_cartas([ 
        Carta('9', ''), 
        Carta('A', ''), 
        Carta('A', '') 
    ]) == 20

    assert dealer.somatorio_cartas([ 
        Carta('7', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', '') 
    ]) == 20

    assert dealer.somatorio_cartas([ 
        Carta('7', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', '') 
    ]) == 19

    assert dealer.somatorio_cartas([ 
        Carta('7', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', '') 
    ]) == 19

    assert dealer.somatorio_cartas([ 
        Carta('8', ''), 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', '') 
    ]) == 20

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
    ]) == 21

    assert dealer.somatorio_cartas([ 
        Carta('A', ''), 
        Carta('A', ''), 
        Carta('A', ''),
        Carta('A', '')
    ]) == 13

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
    ]) == 20

    assert dealer.somatorio_cartas([ 
        Carta('A', ''),
        Carta('A', ''),
        Carta('J', '')
    ]) == 21

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
    dealer = Dealer('teste', 'M')
    jogador = Jogador('teste', 'M')

    jogador.receber_cartas([Carta('A', ''), Carta('A', '')])
    dealer.receber_cartas([Carta('J', ''), Carta('A', '')])
    assert dealer.resultado_jogador(jogador) == 0

def teste_vitoria_jogador_com_blackjack():
    dealer = Dealer('teste', 'M')
    jogador = Jogador('teste', 'M')

    jogador.receber_cartas([Carta('10', ''), Carta('A', ''), Carta('A', '')])
    dealer.receber_cartas([Carta('J', ''), Carta('A', '')])
    assert dealer.resultado_jogador(jogador) == 1      

def teste_derrota_jogador_com_soma_maior_que_21():
    dealer = Dealer('teste', 'M')
    jogador = Jogador('teste', 'M')

    jogador.receber_cartas([Carta('A', ''), Carta('A', ''), Carta('10', ''), Carta('10', '')])
    dealer.receber_cartas([Carta('J', ''), Carta('2', '')])
    assert dealer.resultado_jogador(jogador) == -1