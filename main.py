# cartas de 2-10 valem o valor do número na face da carta.
# Cartas numeradas valem o número correspondente indicado 
# na carta. As cartas de rosto (aquelas com imagens) 
# valem 10, exceto para o Ás, que vale 1 ou 11. Uma 
# imagem combinada com um Ás é Blackjack (um valor de 21).

# TODO: Usar emojis para os naipes das cartas
# Para usar os emojis de cartas:
# Espada :spades:
# Copas  :hearts:
# Paus   :clubs:
# Ouro   :diamonds:

import emoji
from random import shuffle

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f'{self.valor}{self.naipe}'

def criar_baralho():
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
            carta = Carta(valor, naipe)
            baralho.append(carta)

    return baralho

def embaralhar(baralho):
    shuffle(baralho)

baralho = criar_baralho()

embaralhar(baralho)

print(baralho.pop())
print(baralho.pop())
print(baralho.pop())
print(baralho.pop())
print(baralho.pop())