num_see = int(input())
num_mount = int(input())
sums = 0
while True:
    command = input()
    if command == 'Stop':
        break
    if command == 'sea':
        if num_see <= 0:
            continue
        num_see -= 1
        sums += 680
    elif command == 'mountain':
        if num_mount <= 0:
            continue
        num_mount -= 1
        sums += 499
    if num_mount == 0 and num_see == 0:
        print('Good job! Everything is sold.')
        break
print(f'Profit: {sums} leva.')
