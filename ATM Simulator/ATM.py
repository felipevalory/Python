### Desafio 71

# simulador de caixa eletrônico
# perguntar ao usuário qual valor será sacado (numero inteiro)
# informar quantas cedulas de cada valor serão entregues
# considerar que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1


print('='*30)
print('BANCO DO DINHEIRO'.center(30))
print('='*30)
saque = int(input('Qual o valor do saque? R$ '))
total = saque
cedula = 50
totalced = 0
while True:
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO DO DINHEIRO! Tenha um bom dia!')

