budget = float(input())
num_men = int(input())
price_men = float(input())
sums_decor = budget * 0.10
price_1 = num_men * price_men
if num_men >= 150:
    price_d = price_1 * 0.10
    price_1 = price_1 - price_d
total = sums_decor + price_1
if budget >= total:
    print('Action!')
    print(f'Wingard starts filming with {abs(total - budget):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {abs(budget - total):.2f} leva more.')


