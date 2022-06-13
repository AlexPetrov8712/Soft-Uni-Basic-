import math
n = int(input())
red = 0
orange = 0
yellow = 0
white = 0
black = 0
sums = 0
other = 0
for i in range(1, n + 1):
    color = input()
    if color == 'red':
        red += 1
        sums += 5
    elif color == 'orange':
        orange += 1
        sums += 10
    elif color == 'yellow':
        yellow += 1
        sums += 15
    elif color == 'white':
        white += 1
        sums += 20
    elif color == 'black':
        black += 1
        sums /= 2
    else:
        other += 1
print(f'Total points: {math.floor(sums)}')
print(f'Red balls: {red}')
print(f'Orange balls: {orange}')
print(f'Yellow balls: {yellow}')
print(f'White balls: {white}')
print(f'Other colors picked: {other}')
print(f'Divides from black balls: {math.floor(black)}')

