num = int(input())
wins = 0
loses = 0
total_money = 0
for i in range(num):
    command = input()
    win = 0
    lose = 0
    money = 0
    while True:
        if command == 'Finish':
            if win > lose:
                money *= 1.1
                total_money += money
            else:
                total_money += money
            break
        if command == 'win':
            money += 20
            win += 1
            wins += 1
        elif command == 'lose':
            lose += 1
            loses += 1
        command = input()
if wins > loses:
    print(f'You won the tournament! Total raised money: {total_money * 1.2:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')
