import math
number_guest = int(input())
budget = int(input())
cake = number_guest / 3
price_cake = math.ceil(cake) * 4
egg = number_guest * 2
price_egg = egg * 0.45
all_price = price_cake + price_egg
left_money = abs(all_price - budget)
if budget >= all_price:
    print(f'Lyubo bought {math.ceil(cake)} Easter bread and {egg} eggs.')
    print(f'He has {left_money:.2f} lv. left.')
else:
    print(f'Lyubo doesn\'t have enough money.')
    print(f'He needs {left_money:.2f} lv. more.')