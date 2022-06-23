num_days = int(input())
total_win = 0
total_lose = 0
total_money = 0
for i in range(num_days):
    win = 0
    lose = 0
    money = 0
    while True:
        command = input()
        if command == 'Finish':
            if win > lose:
                total_money += money * 1.1
            else:
                total_money += money
            break
        if command == 'win':
            win += 1
            total_win += 1
            money += 20
        elif command == 'lose':
            lose += 1
            total_lose += 1
if total_win > total_lose:
    print(f'You won the tournament! Total raised money: {total_money * 1.2:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')
