type_cinema = input()
r = int(input())
c = int(input())
income = 0
cinema = r * c
if type_cinema == 'Premiere':
    income = cinema * 12
elif type_cinema == 'Normal':
    income = cinema * 7.50
elif type_cinema == 'Discount':
    income = cinema * 5
print(f'{income:.2f} leva')
