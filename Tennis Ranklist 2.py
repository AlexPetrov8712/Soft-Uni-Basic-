import math
num = int(input())
point = int(input())
win = 0
points = 0
final = 0
num_game = 0
for i in range(num):
    result = input()
    num_game += 1
    if result == 'W':
        win += 1
        points += 2000
    elif result == 'F':
        points += 1200
    else:
        points += 720
    final = point + points
print(f'Final points: {math.floor(final)}')
print(f'Average points: {math.floor(points / num_game)}')
print(f'{win / num * 100:.2f}%')

