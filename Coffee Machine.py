drink = input()
sugar = input()
number = int(input())
price = 0
if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.90
    elif sugar == 'Normal':
        price = 1
    else:
        price = 1.20
if drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1
    elif sugar == 'Normal':
        price = 1.20
    else:
        price = 1.60
if drink == 'Tea':
    if sugar == 'Without':
        price = 0.50
    elif sugar == 'Normal':
        price = 0.60
    else:
        price = 0.70
total = price * number
if sugar == 'Without':
    total *= 0.65
if drink == 'Espresso' and number >= 5:
    total *= 0.75
if total > 15:
    total *= 0.80
print(f'You bought {number} cups of {drink} for {total:.2f} lv.')


