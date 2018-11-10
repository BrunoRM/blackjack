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

# TODO: Tentar criar o design de uma mesa

import blackjack as bj

def main():

    def exibir_cartas_jogador(jogador):
        print(f'{jogador.nome}, suas cartas são: \n{jogador.get_cartas_formatada()}')

    dealer = bj.Dealer('nome_dealer', 'm')
    dealer.iniciar_jogo()

    sexo_correto = False
    while not sexo_correto:
        print('Informe o seu sexo(M/F):')
        sexo = str(input('')).upper()
        sexo_correto = True if sexo in ['M', 'F'] else False
        
    print('Informe seu nome:')
    nome = input('')

    jogador = bj.Jogador(nome, sexo)

    jogador.receber_cartas(dealer.entregar_cartas())

    exibir_cartas_jogador(jogador)

    decisao_escolhida = False
    while not decisao_escolhida:
        print('O que deseja fazer?')
        print('1 - Comprar carta')
        print('2 - Parar')
        decisao = input('')
        decisao_escolhida = True if decisao in ['1', '2'] else False

    if decisao == '1':
        jogador.receber_carta(dealer.entregar_carta())
        exibir_cartas_jogador(jogador)
        somatorio = dealer.validar_blackjack(jogador.cartas())
        print(somatorio)
    else:
        somatorio = dealer.validar_blackjack(jogador.cartas())
        print(somatorio)


if __name__ == "__main__":
    main()