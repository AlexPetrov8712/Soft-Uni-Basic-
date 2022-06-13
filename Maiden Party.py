price = float(input())
num_love = int(input())
num_rose = int(input())
num_keys = int((input()))
num_sceck = int(input())
num_luck = int(input())

total_price = (num_love * 0.60) + (num_rose * 7.20) + (num_keys * 3.60) + (num_sceck * 18.20) + (num_luck * 22)
total = num_love + num_rose + num_keys + num_sceck + num_luck
if total >= 25:
    total_price *= 0.65
total_price *= 0.90
if total_price > price:
    print(f'Yes! {total_price - price:.2f} lv left.')
else:
    print(f'Not enough money! {abs(total_price - price):.2f} lv needed.')