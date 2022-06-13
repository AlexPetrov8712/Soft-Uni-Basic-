num_alu = int(input())
caint_alu = input()
whit_d = input()
price = 0
total = 0
if caint_alu == '90X130':
    price = 110
    if 30 < num_alu <= 60:
        price *= 0.95
    elif num_alu > 60:
        price *= 0.92
elif caint_alu == '100X150':
    price = 140
    if 40 < num_alu <= 80:
        price *= 0.94
    elif num_alu > 80:
        price *= 0.90
elif caint_alu == '130X180':
    price = 190
    if 20 < num_alu <= 50:
        price *= 0.93
    elif num_alu > 50:
        price *= 0.88
elif caint_alu == '200X300':
    price = 250
    if 25 < num_alu <= 50:
        price *= 0.91
    elif num_alu > 50:
        price *= 0.86
total = price * num_alu
if whit_d == 'With delivery':
    total += 60
else:
    total = total
if num_alu > 99:
    total *= 0.96
if num_alu > 10:
    print(f'{total:.2f} BGN')
else:
    print('Invalid order')

