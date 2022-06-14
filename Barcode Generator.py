startNum = input()
finalNum = input()
output = ''

for a in range(int(startNum[0]), int(finalNum[0]) + 1):
    for b in range(int(startNum[1]), int(finalNum[1]) + 1):
        for c in range(int(startNum[2]), int(finalNum[2]) + 1):
            for d in range(int(startNum[3]), int(finalNum[3]) + 1):
                if a % 2 == 1 and b % 2 == 1 and c % 2 == 1 and d % 2 == 1:
                    output += f'{a}{b}{c}{d} '

print(output)