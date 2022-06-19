num_men = int(input())
num_women = int(input())
tables = int(input())

for m in range(1, num_men, tables + 1):
    for w in range(1, num_women, tables + 1):

        print(f'({m} <-> {w}) ({m} <-> {w})')
