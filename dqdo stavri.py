days = int(input())
liters = 0
gradus = 0

for i in range(days):
    batch_liters = float(input())
    batch_degrees = float(input())
    liters += batch_liters
    gradus += batch_liters * batch_degrees

print(f'Liter: {liters:.2f}')
print(f'Degrees: {gradus / liters:.2f}')
if gradus / liters < 38:
    print('Not good, you should baking!')
elif gradus / liters <= 42:
    print('Super!')
elif gradus / liters > 42:
    print('Dilutwhile text !=:)
