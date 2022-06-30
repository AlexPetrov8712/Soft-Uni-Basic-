budget = float(input())
price = 0
number_series = int(input())
for i in range(number_series):
    name_series = input()
    ticket = float(input())
    if name_series == 'Thrones':
        price += (ticket * 0.50)
    elif name_series == 'Lucifer':
        price += (ticket * 0.60)
    elif name_series == 'Protector':
        price += (ticket * 0.70)
    elif name_series == 'TotalDrama':
        price += (ticket * 0.80)
    elif name_series == 'Area':
        price += (ticket * 0.90)
    else:
        price += ticket
if budget >= price:
    print(f'You bought all the series and left with {budget - price:.2f} lv.')
else:
    print(f'You need {price - budget:.2f} lv. more to buy the series!')