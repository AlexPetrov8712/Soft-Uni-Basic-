name_player = input()
points = 301
shots = 0
bad_shots = 0
while True:
    command = input()
    if command == 'Retire':
        print(f'{name_player} retired after {bad_shots} unsuccessful shots.')
        break
    point = int(input())
    if command == 'Single':
        if points <= point:
            bad_shots += 1
            continue
        points -= point
    elif command == 'Double':
        if points <= point:
            bad_shots += 1

        points -= (point * 2)
    elif command == 'Triple':
        if points <= point:
            bad_shots += 1
            continue
        points -= (point * 3)
    shots += 1
    if points == 0:
        print(f'{name_player} won the leg with {shots} shots.')
        break





