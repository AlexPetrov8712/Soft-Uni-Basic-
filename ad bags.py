price_20 = float(input())
kg_bag = float(input())
day_trip = int(input())
number_bag = int(input())
total = 0
if kg_bag < 10:
    total = price_20 * 0.2
elif 10 <= kg_bag <= 20:
    total = price_20 * 0.5
if kg_bag > 20:
    total = price_20
if day_trip > 30:
    total *= 1.10
elif 7 <= day_trip <= 30:
    total *= 1.15
elif day_trip < 7:
    total *= 1.40
print(f'The total price of bags is: {total * number_bag:.2f} lv.')


