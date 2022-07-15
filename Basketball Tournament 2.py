win = 0
loseses = 0
count = 0
while True:
    name = input()
    if name == 'End of tournaments':
        print(f'{win / count * 100:.2f}% matches win')
        print(f'{loseses / count * 100:.2f}% matches lost')
        break
    count_tournament = int(input())
    result = 0
    num_game = 0
    for i in range(count_tournament):
        count += 1
        num_game += 1
        point1 = int(input())
        point2 = int(input())
        if point1 > point2:
            result = point1 - point2
            win += 1
            print(f'Game {num_game} of tournament {name}: win with {result} points.')
        else:
            result = point2 - point1
            loseses += 1
            print(f'Game {num_game} of tournament {name}: lost with {result} points.')


