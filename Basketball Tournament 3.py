
win = 0
lose = 0
count_games = 0
while True:
    name = input()
    if name == 'End of tournaments':
        print(f'{win / count_games * 100:.2f}% matches win')
        print(f'{lose / count_games * 100:.2f}% matches lost')
        break
    games = int(input())
    game = 0
    result = 0
    for i in range(games):
        game += 1
        count_games += 1
        team1 = int(input())
        team2 = int(input())
        if team1 > team2:
            result = team1 - team2
            win += 1
            print(f'Game {game} of tournament {name}: win with {result} points.')
        else:
            result = team2 - team1
            lose += 1
            print(f'Game {game} of tournament {name}: lost with {result} points.')
