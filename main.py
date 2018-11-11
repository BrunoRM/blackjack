import blackjack as bj
import os
import emoji

def main():

    def exibir_cartas_jogador(jogador: bj.Jogador):
        print(f'{jogador.cartas_str()}')

    def limpar_tela():
        os.system('cls')
        os.system('clear')

    def mensagem_vitoria_jogador(jogador):
        print(f'Parabéns {jogador.nome()}, você venceu a rodada! {emoji.emojize(":clap:"*10, use_aliases=True)}')

    def mensagem_derrota_jogador(jogador):
        print(f'{jogador.nome()}, você perdeu a rodada {emoji.emojize(":thumbsdown:", use_aliases=True)}')

    def mensagem_empate():
        print(f'Empate!!')

    limpar_tela()
    print('=============================')
    print(' Seja bem-vindo ao blackjack')
    print('=============================')

    dealer = bj.Dealer()

    nome_correto = False
    while not nome_correto:
        print('Informe seu nome:')
        nome = str(input(''))        
        if len(nome.strip()) > 0: 
            nome_correto = True
        else: 
            print(f'Nome inválido')
            limpar_tela()

    jogador = bj.Jogador(nome)
    continuar_jogando = True
    while continuar_jogando:    
        dealer.iniciar_jogo()
        limpar_tela()
        jogador.receber_cartas(dealer.entregar_cartas_jogador())    

        # Caso o jogador já tenha 21 no entregar das cartas
        somatorio_jogador = dealer.somatorio_cartas(jogador.cartas())
        escolher_decisao = True if somatorio_jogador < 21 else False
        while escolher_decisao:
            # limpar_tela()
            print(f'{jogador.nome()}, suas cartas são: ')
            exibir_cartas_jogador(jogador)
            print('O que deseja fazer?')
            print('1 - Comprar carta')
            print('2 - Parar de jogar')
            decisao = str(input(''))
            if decisao not in ['1', '2']:                
                continue
            else:
                limpar_tela()
                if decisao == '1':
                    jogador.receber_carta(dealer.entregar_carta())                    
                    somatorio_jogador = dealer.somatorio_cartas(jogador.cartas())
                    if somatorio_jogador == 21: escolher_decisao = False
                    elif somatorio_jogador > 21: escolher_decisao = False
                    else: continue
                else:
                    escolher_decisao = False

        resultado = dealer.resultado_jogador(jogador)
        if resultado == -1:
            mensagem_derrota_jogador(jogador)                    
        elif resultado == 0:
            mensagem_empate()                        
        else:
            mensagem_vitoria_jogador(jogador)

        print(f'Suas cartas: {jogador.cartas_str()}({dealer.somatorio_cartas(jogador.cartas())})')
        print(f'Cartas do Dealer: {dealer.cartas_str()}({dealer.somatorio_cartas(dealer.cartas())})')
        dealer.receber_cartas_jogador(jogador.entregar_cartas())
        print('Deseja jogar novamente?')
        continuar_jogando = True if str(input()).upper() == 'S' else False

if __name__ == "__main__":
    main()