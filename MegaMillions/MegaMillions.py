from random import randint
from time import sleep

temporary_list = list()
bets = list()
print('-'*40)
print('MEGA MILLIONS'.center(40))
print('-'*40)

num_bet = int(input('How many bets do you want me to draw? '))
print()
print('-='*5, f'DRAWING {num_bet} BETS', '-='*5)
print()
total = 1
while total <= num_bet:
    count_ = 0
    while True:
        num = randint(1, 70)
        if num not in temporary_list:
            temporary_list.append(num)
            count_ += 1
        if count_ >= 6:
            break
    temporary_list.sort()
    bets.append(temporary_list[:])
    temporary_list.clear()
    total += 1
for i, l in enumerate(bets):
    print(f'Bet {i+1}: {l}')
    sleep(0.3)
print()
print('-='*7, 'GOOD LUCK', '-='*7)

