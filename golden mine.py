location = int(input())
total = 0
for i in range(location):
    expected_gold = float(input())
    day = int(input())
    gold = 0
    for n in range(day):
        gold += float(input())
    if expected_gold > gold / day:
        total = abs(expected_gold - (gold / day))
        print(f'You need {total:.2f} gold.')
    else:
        print(f'Good job! Average gold per day: {gold / day:.2f}.')
