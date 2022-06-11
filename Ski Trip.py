day = int(input())
type_room = input()
evaluation = input()
room_one_person = 18.00
apartment = 25
president_apartment = 35
price = 0
day -= 1
if type_room == 'room for one person':
    price = room_one_person * day
elif type_room == 'apartment':
    price = apartment * day
    if day < 10:
        discount = price * 0.30
        price = price - discount
    elif 10 <= day <= 15:
        discount = price * 0.35
        price = price - discount
    elif day > 15:
        discount = price * 0.50
        price = price - discount
elif type_room == 'president apartment':
    price = president_apartment * day
    if day < 10:
        discount = price * 0.10
        price = price - discount
    elif 10 <= day <= 15:
        discount = price * 0.15
        price = price - discount
    elif day > 15:
        discount = price * 0.20
        price = price - discount
if evaluation == 'positive':
    discount = price * 0.25
    price = price + discount
else:
    discount = price * 0.10
    price = price - discount
print(f'{price:.2f}')
