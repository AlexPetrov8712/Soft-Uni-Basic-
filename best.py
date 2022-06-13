best_player = ''
goals = 0
command = input()
while command != "END":
    goal = int(input())
    if goal > goals:
        best_player = command
        goals = goal
    if goals >= 10:
        break
    command = input()
print(f'{best_player} is the best player!')
if goals < 3:
    print(f'He has scored {goals} goals.')
else:
    print(f'He has scored {goals} goals and made a hat-trick !!!')
