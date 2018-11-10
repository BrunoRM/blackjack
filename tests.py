import blackjack as bj

def teste_validar_blackjack():
    dealer = bj.Dealer('teste', 'F')

    assert dealer.validar_blackjack([ 
        bj.Carta('9', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus') 
    ]) == 20

    assert dealer.validar_blackjack([ 
        bj.Carta('7', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus') 
    ]) == 20

    assert dealer.validar_blackjack([ 
        bj.Carta('7', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus') 
    ]) == 19

    assert dealer.validar_blackjack([ 
        bj.Carta('7', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus') 
    ]) == 19

    assert dealer.validar_blackjack([ 
        bj.Carta('8', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus') 
    ]) == 20

    assert dealer.validar_blackjack([ 
        bj.Carta('9', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'),
        bj.Carta('A', 'paus')
    ]) == 13

    assert dealer.validar_blackjack([ 
        bj.Carta('10', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'),
        bj.Carta('A', 'paus')
    ]) == 14

    assert dealer.validar_blackjack([ 
        bj.Carta('J', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('3', 'paus')
    ]) == 15

    assert dealer.validar_blackjack([ 
        bj.Carta('J', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus')
    ]) == 21

    assert dealer.validar_blackjack([ 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'),
        bj.Carta('A', 'paus')
    ]) == 13

    assert dealer.validar_blackjack([ 
        bj.Carta('2', 'paus'), 
        bj.Carta('5', 'paus'), 
        bj.Carta('9', 'paus'),
        bj.Carta('A', 'paus')
    ]) == 17

    assert dealer.validar_blackjack([ 
        bj.Carta('2', 'paus'), 
        bj.Carta('6', 'paus'), 
        bj.Carta('9', 'paus'),
        bj.Carta('4', 'paus')
    ]) == 21

    assert dealer.validar_blackjack([ 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus')
    ]) == 20

    assert dealer.validar_blackjack([ 
        bj.Carta('A', 'paus'),
        bj.Carta('A', 'paus'),
        bj.Carta('J', 'paus')
    ]) == 21

    assert dealer.validar_blackjack([ 
        bj.Carta('10', 'paus'), 
        bj.Carta('J', 'paus'), 
        bj.Carta('A', 'paus'),
        bj.Carta('A', 'paus')
    ]) == 22

    assert dealer.validar_blackjack([ 
        bj.Carta('10', 'paus'), 
        bj.Carta('J', 'paus'), 
        bj.Carta('A', 'paus'),
        bj.Carta('A', 'paus'),
        bj.Carta('A', 'paus')
    ]) == 23

    assert dealer.validar_blackjack([ 
        bj.Carta('10', 'paus'), 
        bj.Carta('J', 'paus'), 
        bj.Carta('2', 'paus'),
        bj.Carta('2', 'paus'),
        bj.Carta('A', 'paus')
    ]) == 25

    assert dealer.validar_blackjack([ 
        bj.Carta('10', 'paus'), 
        bj.Carta('J', 'paus'), 
        bj.Carta('2', 'paus'),
        bj.Carta('2', 'paus'),
        bj.Carta('A', 'paus')
    ]) == 25

    assert dealer.validar_blackjack([ 
        bj.Carta('10', 'paus'), 
        bj.Carta('J', 'paus'), 
        bj.Carta('3', 'paus'),
        bj.Carta('A', 'paus')
    ]) == 24

    assert dealer.validar_blackjack([ 
        bj.Carta('10', 'paus'), 
        bj.Carta('J', 'paus'), 
        bj.Carta('3', 'paus'),
        bj.Carta('A', 'paus'),
        bj.Carta('A', 'paus')
    ]) == 25

    assert dealer.validar_blackjack([ 
        bj.Carta('10', 'paus'), 
        bj.Carta('A', 'paus'), 
        bj.Carta('A', 'paus'),
        bj.Carta('J', 'paus')
    ]) == 22