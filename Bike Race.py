juniors = int(input())
seniors = int(input())
trace = input()
price_juniors = 0
price_seniors = 0
total_man = juniors + seniors
if trace == 'trail':
    price_juniors = 5.50 * juniors
    price_seniors = 7 * seniors
elif trace == 'cross-country':
    price_juniors = 8 * juniors
    price_seniors = 9.50 * seniors
elif trace == 'downhill':
    price_juniors = 12.25 * juniors
    price_seniors = 13.75 * seniors
else:
    price_juniors = 20 * juniors
    price_seniors = 21.50 * seniors
total = price_seniors + price_juniors
if total_man >= 50 and trace == 'cross-country':
    total *= 0.75
total *= 0.95
print(f'{total:.2f}')
