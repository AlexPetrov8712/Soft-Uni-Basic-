trips = input()
date = input()
number = int(input())
price = 0
if trips == 'France':
    if date == '21-23':
        price = 30
    elif date == '24-27':
        price = 35
    elif date == '28-31':
        price = 40
if trips == 'Italy':
    if date == '21-23':
        price = 28
    elif date == '24-27':
        price = 32
    elif date == '28-31':
        price = 39
if trips == 'Germany':
    if date == '21-23':
        price = 32
    elif date == '24-27':
        price = 37
    elif date == '28-31':
        price = 43
total = price * number
print(f'Easter trip to {trips} : {total:.2f} leva.')

