food = int(input()) * 1000
total = 0
while True:
    command = input()
    if command == 'Adopted':
        if food >= total:
            print(f'Food is enough! Leftovers: {food - total} grams.')
        else:
            print(f'Food is not enough. You need {total - food} grams more.')
        break
    left_food = int(command)
    total += left_food
