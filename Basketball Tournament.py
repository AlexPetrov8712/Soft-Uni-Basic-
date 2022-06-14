games = 0
wins = 0
lose = 0
while True:
    command = input()
    if command == 'End of tournaments':
        print(f'{wins / games * 100:.2f}% matches win')
        print(f'{lose / games * 100:.2f}% matches lost')
        break
    num_games = int(input())
    count_game = 0
    for i in range(num_games):
        games += 1
        count_game += 1
        team1 = int(input())
        team2 = int(input())
        if team1 > team2:
            wins += 1
            print(f'Game {count_game} of tournament {command}: win with {team1 - team2} points.')
        elif team2 > team1:
            lose += 1
            print(f'Game {count_game} of tournament {command}: lost with {abs(team1 - team2)} points.')

