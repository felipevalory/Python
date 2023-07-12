from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Escolha uma opção abaixo:
      
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
      ''')

while True:
    jogador = input('Sua escolha: ')

    if jogador.isdigit:
        try:
            jogador_int = int(jogador)
            
            computador = randint(0,2)
            print('JO')
            sleep(0.5)
            print('KEN')
            sleep(0.5)
            print('PÔ!')
            print('-='*11)
            
            print(f'O computador escolheu {itens[computador]} e você {itens[jogador_int]}')

            if computador == 0:
                if jogador_int == 0:
                        print('Deu empate! 💁')
                elif jogador_int == 1:
                    print('Parabéns, você ganhou! 🎉')
                elif jogador_int == 2:
                    print('Que pena, você perdeu! 😔 Tente novamente!')
                else:
                    print('JOGADA INVÁLIDA!')
            elif computador == 1:
                if jogador_int == 0:
                    print('Que pena, você perdeu! 😔 Tente novamente!')
                elif jogador_int == 1:
                    print('Deu empate! 💁')
                elif jogador_int == 2:
                    print('Parabéns, você ganhou! 🎉')
                else:
                    print('JOGADA INVÁLIDA!')
            elif computador == 2:
                if jogador_int == 0:
                    print('Parabéns, você ganhou! 🎉')
                elif jogador_int == 1:
                    print('Que pena, você perdeu! 😔 Tente novamente!')
                elif jogador_int == 2:
                    print('Deu empate! 💁')
                else:
                    print('JOGADA INVÁLIDA!')
                  
        except ValueError:
            print('Por favor, digite um número válido!')
        except IndexError:
            print('Valor não encontrado. Escolha um número válido')


