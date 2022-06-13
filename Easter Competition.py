number_bake = int(input())
command = input()
best = ''
total = 0
while command != 'Stop':
    number_bake = int(input())
    total = 0
    if command == 'Stop':
        break
    for i in range(number_bake):
        point = int(input())
        total += point



