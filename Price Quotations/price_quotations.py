from time import sleep
price_quotation = list()
while True:
    product = str(input("Product's name: "))
    price1 = input('Price 1: ')
    price2 = input('Price 2: ')
    price3 = input('Price 3: ')
    valid_prices = None
    price1_float = 0
    price2_float = 0
    price3_float = 0

    try:
        price1_float = float(price1)
        price2_float = float(price2)
        price3_float = float(price3)
        valid_prices = True

    except:
        valid_prices = None

    if valid_prices is None:
        print('Please, at least one of the prices is invalid. Try again.')
        continue

    average = (price1_float + price2_float + price3_float) / 3
    price_quotation.append(
        [product, [price1_float, price2_float, price3_float], average]
    )
    answer = str(input('Do you to input more procucts [Y/N]? ')).upper()[0]
    if answer in 'N':
        break

print('-'*30)
print(f'{"No.":<4}{"PRODUCT":<10}{"AVERAGE":>8}')
print('-'*26)

for i, p in enumerate(price_quotation):
    print(f'{i:<4}{p[0]:<10}{p[2]:>8.1f}')

while True:
    print('-'*26)
    option = int(input(
        "What products prices do you want to see ? (999 stop): "
    ))

    if option == 999:
        print('FINISHING...')
        sleep(0.5)
        break

    if option <= len(price_quotation)-1:
        print(f'Prices of {price_quotation[option][0]}: ')
        print()
        for c in price_quotation[option][1]:
            print(f'{c}')

print('<<< COME BACK ANYTIME >>>')
