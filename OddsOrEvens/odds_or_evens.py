### Desafio 68

# jogo do par ou impar com o pc
# jog interrompido quando o jogador perder
# mostrar total de vitorias consecutivas que conquistou no final do jogo

print('=-'*15)
print('Vamos jogar par ou ímpar')
print('=-'*15)
from random import randint
c = 0
while True:
    valor = int(input('Digite um número inteiro de 0 a 10: '))
    computador = randint(0, 10)
    soma = valor + computador
    opcao = ' '
    c += 1
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar [P/I]? ')).upper().strip()[0]
    if opcao =='P' and soma % 2 == 0:
        print(f'\nVocê jogou {valor} e o computador {computador}. Total de {soma} -> DEU PAR\n')
        print('\nVocê venceu!!👏 Vamos jogar novamente...\n')
    if opcao == 'I' and soma % 2 != 0:
        print(f'\nVocê jogou {valor} e o computador {computador}. Total de {soma} -> DEU ÍMPAR')
        print('\nVocê venceu!!👏 Vamos jogar novamente...\n')
    if opcao == 'P' and soma % 2 != 0:
        print(f'\nVocê jogou {valor} e o computador {computador}. Total de {soma} -> DEU ÍMPAR')
        print('\nVocê perdeu!')
        break
    if opcao == 'I' and soma % 2 == 0:
        print(f'\nVocê jogou {valor} e o computador {computador}. Total de {soma} -> DEU PAR')
        print('\nVocê perdeu!')
        break
if c == 1:
    print(f'\nGame Over! Você venceu {0} vezes.😔')
    print('=-'*17)
else:
    print(f'\nGame Over! Você venceu {c-1} vezes.🏆')
    print('=-'*17)







