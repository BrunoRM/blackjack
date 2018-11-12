import emoji
from random import shuffle
from typing import List

class Carta:
    def __init__(self, valor, naipe):
        self.__valor = valor
        self.__naipe = naipe

    def valor(self):
        return self.__valor

    def __str__(self):
        return f'{self.__valor}{self.__naipe}'

class Dealer:
    def __init__(self):
        self.__baralho = self.__criar_baralho()
        self.__descartes = []
        self.__cartas = []

    def __embaralhar(self):        
        shuffle(self.__baralho)

    def __criar_baralho(self):
        cartas = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        naipes = (
            emoji.emojize(':spades:', use_aliases=True), 
            emoji.emojize(':hearts:', use_aliases=True),
            emoji.emojize(':clubs:', use_aliases=True),
            emoji.emojize(':diamonds:', use_aliases=True)
        )

        baralho = []
        for valor in cartas:
            for naipe in naipes:
                baralho.append(Carta(valor, naipe))

        return baralho

    def iniciar_jogo(self):
        # Devolver as cartas descartadas no ínicio da rodada
        if len(self.__descartes) > 0:
            for carta in self.__descartes:
                self.__baralho.append(carta)

        # Devolver as cartas do Dealer para o baralho
        if len(self.__cartas) > 0:
            for carta in self.__cartas:
                self.__baralho.append(carta)
        
        self.__embaralhar()

        # No inicio da rodada serão descartadas 5 cartas e entregues 2 ao Dealer
        self.__descartes = [self.__baralho.pop() for _ in range(0, 5)]
        self.__cartas = [self.__baralho.pop() for _ in range(0, 2)]

    def receber_cartas(self, cartas):
        for carta in cartas:
            self.__cartas.append(carta)

    def receber_cartas_jogador(self, cartas):
        for carta in cartas:
            self.__baralho.append(carta)

    def entregar_cartas_jogador(self):
        return [self.__baralho.pop(), self.__baralho.pop()]

    def entregar_carta(self):
        return self.__baralho.pop()

    def somatorio_cartas(self, cartas_jogador: List[Carta]):

        def somatorio_as(soma, qtd_as):
            s = 0
            soma_aux = 0
            for i in range(0, qtd_as+1):
                soma_aux = soma + (11 * (qtd_as - i)) + i
                
                if soma_aux > s and soma_aux <= 21: s = soma_aux
                elif soma_aux > s and (s > 21 or s == 0): s = soma_aux
                elif soma_aux < s and s > 21: s = soma_aux
                
            return s

        cartas_as = []
        soma = 0
        for carta in cartas_jogador:
            if carta.valor() == 'A': cartas_as.append(carta)
            elif carta.valor() in ['J', 'Q', 'K']: soma += 10
            else: soma += int(carta.valor())

        if len(cartas_as) > 0:
            soma = somatorio_as(soma, len(cartas_as))

        return soma

    def quantidade_cartas_baralho(self):
        return len(self.__baralho)

    def resultado_jogador(self, jogador):
        # -1 = Derrota do jogador, 0 = Empate, 1 = Vitória do jogador
        soma_jogador = self.somatorio_cartas(jogador.cartas())
        if soma_jogador > 21:
            return -1
        else:
            soma_dealer = self.somatorio_cartas(self.__cartas)
            if soma_dealer == 21 and soma_jogador == 21:
                return 0
            elif soma_dealer == 21:
                return -1
            elif soma_dealer > soma_jogador and soma_dealer < 21:
                return -1            
            elif soma_dealer < soma_jogador:
                pode_jogar = True
                while pode_jogar:
                    self.__cartas.append(self.entregar_carta())
                    soma_dealer = self.somatorio_cartas(self.__cartas)
                    if soma_dealer == soma_jogador:
                        return 0
                    elif soma_dealer == 21:
                        return -1
                    elif soma_dealer > 21:
                        return 1
                    elif soma_dealer < 21 and soma_dealer < soma_jogador:
                        continue
                    elif soma_dealer < 21 and soma_dealer > soma_jogador:
                        return -1
            else:
                return 0

    def cartas(self):
        return self.__cartas

    def cartas_str(self):
        cartas = ''
        for carta in self.__cartas:
            cartas += f'{carta} '
        return cartas

class Jogador:
    def __init__(self, nome):
        self.__nome = nome
        self.__cartas = []

    def receber_cartas(self, cartas_recebidas):
        for carta in cartas_recebidas:
            self.__cartas.append(carta)

    def nome(self):
        return self.__nome

    def cartas_str(self):
        cartas = ''
        for carta in self.__cartas:
            cartas += f'{carta} '
        return cartas

    def cartas(self):
        return self.__cartas

    def entregar_cartas(self):
        return [self.__cartas.pop() for _ in range(0, len(self.__cartas))]    

    def receber_carta(self, carta_recebida):
        self.__cartas.append(carta_recebida)