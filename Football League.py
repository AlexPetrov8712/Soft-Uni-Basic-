capacity = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
people = int(input())
for i in range(people):
    sector = input()
    if sector == 'A':
        sector_a += 1
    elif sector == 'B':
        sector_b += 1
    elif sector == 'V':
        sector_v += 1
    elif sector == 'G':
        sector_g += 1
print(f'{sector_a / people * 100:.2f}%')
print(f'{sector_b / people * 100:.2f}%')
print(f'{sector_v / people * 100:.2f}%')
print(f'{sector_g / people * 100:.2f}%')
print(f'{people / capacity * 100:.2f}%')