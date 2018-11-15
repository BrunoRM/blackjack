from random import shuffle
from typing import List

class Carta:
    def __init__(self, valor, naipe):
        self._valor = valor
        self._naipe = naipe

    def valor(self):
        return self._valor

    def __str__(self):
        return f'{self._valor}{self._naipe}'

class Dealer:
    def __init__(self):
        self._baralho = self._criar_baralho()
        self._descartes = []
        self._cartas = []

    def _embaralhar(self):        
        shuffle(self._baralho)

    def _criar_baralho(self):
        cartas = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        naipes = ('\u2660','\u2665','\u2666','\u2663') # Espada, Copas, Ouros, Paus
        baralho = []

        for valor in cartas:
            for naipe in naipes:
                baralho.append(Carta(valor, naipe))

        return baralho

    def iniciar_jogo(self):
        # Devolver as cartas descartadas no ínicio da rodada
        if len(self._descartes) > 0:
            for carta in self._descartes:
                self._baralho.append(carta)

        # Devolver as cartas do Dealer para o baralho
        if len(self._cartas) > 0:
            for carta in self._cartas:
                self._baralho.append(carta)
        
        self._embaralhar()

        # No inicio da rodada serão descartadas 5 cartas e entregues 2 ao Dealer
        self._descartes = [self._baralho.pop() for _ in range(0, 5)]
        self._cartas = [self._baralho.pop() for _ in range(0, 2)]

    def receber_cartas(self, cartas):
        for carta in cartas:
            self._cartas.append(carta)

    def receber_cartas_jogador(self, cartas):
        for carta in cartas:
            self._baralho.append(carta)

    def entregar_cartas_jogador(self):
        cartas = []
        cartas.append(self._baralho.pop())
        cartas.append(self._baralho.pop())
        return cartas

    def entregar_carta(self):
        return self._baralho.pop()

    def somatorio_cartas(self, cartas_jogador: List[Carta]):

        def somatorio_as(soma, qtd_as):
            s = 0
            soma_aux = 0
            for i in range(0, qtd_as+1):
                soma_aux = soma + (11 * (qtd_as - i)) + i
                
                if soma_aux > s and soma_aux <= 21: 
                    s = soma_aux
                elif soma_aux > s and (s > 21 or s == 0): 
                    s = soma_aux
                elif soma_aux < s and s > 21: 
                    s = soma_aux
                
            return s

        cartas_as = []
        soma = 0
        for carta in cartas_jogador:
            if carta.valor() == 'A': 
                cartas_as.append(carta)
            elif carta.valor() in ['J', 'Q', 'K']: 
                soma += 10
            else: 
                soma += int(carta.valor())

        if len(cartas_as) > 0:
            soma = somatorio_as(soma, len(cartas_as))

        return soma

    def quantidade_cartas_baralho(self):
        return len(self._baralho)

    def resultado_jogador(self, jogador):
        # -1 = Derrota do jogador, 0 = Empate, 1 = Vitória do jogador
        soma_jogador = self.somatorio_cartas(jogador.cartas())
        if soma_jogador > 21:
            return -1
        else:
            soma_dealer = self.somatorio_cartas(self._cartas)
            if soma_dealer == 21 and soma_jogador == 21:
                return 0
            elif soma_dealer == 21 or (soma_dealer > soma_jogador and soma_dealer < 21):
                return -1        
            elif soma_dealer < soma_jogador:
                pode_jogar = True
                while pode_jogar:
                    self._cartas.append(self.entregar_carta())
                    soma_dealer = self.somatorio_cartas(self._cartas)
                    if soma_dealer == soma_jogador:
                        return 0
                    elif soma_dealer == 21 or (soma_dealer < 21 and soma_dealer > soma_jogador):
                        return -1
                    elif soma_dealer > 21:
                        return 1
                    elif soma_dealer < 21 and soma_dealer < soma_jogador:
                        continue
            else:
                return 0

    def cartas(self):
        return self._cartas

    def cartas_str(self):
        cartas = ''
        for carta in self._cartas:
            cartas += f'{carta} '
        return cartas

class Jogador:
    def __init__(self, nome):
        self._nome = nome
        self._cartas = []

    def receber_cartas(self, cartas_recebidas):
        for carta in cartas_recebidas:
            self._cartas.append(carta)

    def nome(self):
        return self._nome

    def cartas_str(self):
        cartas = ''
        for carta in self._cartas:
            cartas += f'{carta} '
        return cartas

    def cartas(self):
        return self._cartas

    def entregar_cartas(self):
        return [self._cartas.pop() for _ in range(0, len(self._cartas))]    

    def receber_carta(self, carta_recebida):
        self._cartas.append(carta_recebida)