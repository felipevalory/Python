print('=-'*15)
print("Let's play odds or evens")
print('=-'*15)
from random import randint
count = 0
while True:
    value = int(input('Enter an integer number from 0 to 10: '))
    computer = randint(0, 10)
    total_sum = value + computer
    option = ' '
    count += 1
    while option not in 'OE':
        option = str(input('Odds or Evens [O/E]? ')).upper().strip()[0]
    if option =='E' and total_sum % 2 == 0:
        print(f'\nYou entered {value} and the computer {computer}. Total of {total_sum} -> EVEN\n')
        print("\nYou win!!👏 Let's play again...\n")
    if option == 'O' and total_sum % 2 != 0:
        print(f'\nYou entered {value} and the computer {computer}. Total of {total_sum} -> ODD')
        print("\nYou win!!👏 Let's play again...\n")
    if option == 'O' and total_sum % 2 != 0:
        print(f'\nYou entered {value} and the computer {computer}. Total of {total_sum} -> ODD')
        print('\nYou lose!')
        break
    if option == 'E' and total_sum % 2 == 0:
        print(f'\nYou entered {value} and the computer {computer}. Total of {total_sum} -> EVEN')
        print('\nYou lose!')
        break
if count == 1:
    print(f'\nGame Over! You won {0} times.😔')
    print('=-'*17)
else:
    print(f'\nGame Over! You won {count-1} times.🏆')
    print('=-'*17)







