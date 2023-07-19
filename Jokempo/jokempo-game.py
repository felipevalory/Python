from random import randint
from time import sleep
items = ('Rock', 'Paper', 'Scissors')
print('''Choose an option below:
      
[ 0 ] Rock
[ 1 ] Paper
[ 2 ] Scissors
      ''')

while True:
    player = input('Your turn: ')

    if player.isdigit:
        try:
            player_int = int(player)
            
            computer = randint(0,2)
            print('JO')
            sleep(0.5)
            print('KEN')
            sleep(0.5)
            print('PÔ!')
            print('-='*11)
            
            print(f'The computer chose {items[computer]} and you {items[player_int]}')

            if computer == 0:
                if player_int == 0:
                        print('Tied! 💁')
                elif player_int == 1:
                    print('Congrats! You win! 🎉')
                elif player_int == 2:
                    print('What a shame, you lose! 😔 Try it again!')
                else:
                    print('INVALID MOVE!')
            elif computer == 1:
                if player_int == 0:
                    print('What a shame, you lose! 😔 Try it again!')
                elif player_int == 1:
                    print('Tied! 💁')
                elif player_int == 2:
                    print('Congrats! You win! 🎉')
                else:
                    print('INVALID MOVE!')
            elif computer == 2:
                if player_int == 0:
                    print('Congrats! You win! 🎉')
                elif player_int == 1:
                    print('What a shame, you lose! 😔 Try it again!')
                elif player_int == 2:
                    print('Tied! 💁')
                else:
                    print('INVALID MOVE!')
                  
        except ValueError:
            print('Please, enter a valid number!')
        except IndexError:
            print('Number not found. Choose a valid number')


