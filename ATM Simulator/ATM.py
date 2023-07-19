print('='*30)
print("MONEY'S BANK".center(30))
print('='*30)
withdraw = int(input('What is the withdraw amount? U$ '))
total = withdraw
banknote = 50
total_banknote = 0
while True:
    if total >= banknote:
        total -= banknote
        total_banknote += 1
    else:
        if total_banknote > 0:
            print(f'Total of {total_banknote} banknotes of U$ {banknote}')
        if banknote == 50:
            banknote = 20
        elif banknote == 20:
            banknote = 10
        elif banknote == 10:
            banknote = 1
        total_banknote = 0
        if total == 0:
            break
print('='*30)
print("Come back anytime at MONEY'S BANK! Have a nice day!")

