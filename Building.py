floors = int(input())
rooms = int(input())
rooms_count = 0
room_name = ''
for floor in range(floors, 0, - 1):
    for room in range(rooms):
        rooms_count = floor * 10 + room
        if floor == floors:
            room_name = f'L{rooms_count} '
        elif floor % 2 != 0:
            room_name = f'A{rooms_count} '
        elif floor % 2 == 0:
            room_name = f'O{rooms_count} '
        print(room_name, end='')
    print()




