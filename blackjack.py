import emoji
from random import shuffle
from typing import List

# Classe Carta
class Carta:
    def __init__(self, valor, naipe):
        self.__valor = valor
        self.__naipe = naipe

    def valor(self):
        return self.__valor

    def __str__(self):
        return f'{self.__valor}{self.__naipe}'

# Classe Dealer
class Dealer:
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo
        self.__baralho = self.__criar_baralho()
        self.descartes = []

    def __embaralhar(self):        
        shuffle(self.__baralho)

    def __criar_baralho(self):
        naipes = (
            emoji.emojize(':spades:', use_aliases=True), 
            emoji.emojize(':hearts:', use_aliases=True),
            emoji.emojize(':clubs:', use_aliases=True),
            emoji.emojize(':diamonds:', use_aliases=True)
        )

        cartas = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

        baralho = []
        for valor in cartas:
            for naipe in naipes:
                baralho.append(Carta(valor, naipe))

        return baralho

    def iniciar_jogo(self):
        # Quando houver cartas descartadas, elas deverão
        # ser devolvidas para o baralho no inicio da rodada
        if len(self.descartes) > 0:
            for carta in self.descartes:
                self.__baralho.append(carta)
        
        self.__embaralhar()
        for i in range(1, 6):
            # No inicio da rodada serão descartadas 5 cartas...
            self.descartes.append(self.__baralho.pop())

    def entregar_cartas(self):
        cartas = [self.__baralho.pop(), self.__baralho.pop()]
        return cartas

    def entregar_carta(self):
        return self.__baralho.pop()

    def __validar_melhor_combinacao_de_as(self, soma, qtd_as):
        s = 0
        soma_aux = 0
        for i in range(0, qtd_as+1):
            soma_aux = soma + (10 * (qtd_as - i)) + i

            if soma_aux > s and soma_aux <= 21: s = soma_aux
            elif soma_aux > s and (s > 21 or s == 0): s = soma_aux
            elif soma_aux < s and s > 21: s = soma_aux
            
        return s

    def validar_blackjack(self, cartas_jogador: List[Carta]):

        cartas_as = []
        soma = 0
        for carta in cartas_jogador:
            if carta.valor() == 'A': cartas_as.append(carta)
            elif carta.valor() in ['J', 'Q', 'K']: soma += 10
            else: soma += int(carta.valor())

        if len(cartas_as) > 0:
            soma = self.__validar_melhor_combinacao_de_as(soma, len(cartas_as))

        return soma

    def __str__(self):
        return f'Dealer {self.nome}'

# Classe jogador
class Jogador:
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo
        # Adicionar emoji correspondente
        if (sexo == 'M'):
            pass
        else:
            pass
        self.__cartas = []

    def receber_cartas(self, cartas_recebidas):
        for carta in cartas_recebidas:
            self.__cartas.append(carta)

    def get_cartas_formatada(self):
        fcartas = ''
        for carta in self.__cartas:
            fcartas += f'{carta} '
        return fcartas

    def cartas(self):
        return self.__cartas

    def receber_carta(self, carta_recebida):
        self.__cartas.append(carta_recebida)