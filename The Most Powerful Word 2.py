
winner = ''
max_score = 0
while True:
    name = input()
    if name == 'Stop':
        break
    point = 0
    for i in range(len(name)):
        num = int(input())
        if ord(name[i]) == num:
            point += 10
        else:
            point += 2
        if point >= max_score:
            max_score = point
            winner = name
print(f'The winner is {winner} with {max_score} points!')
