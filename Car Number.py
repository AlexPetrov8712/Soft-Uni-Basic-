num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    for n in range(num1, num2 + 1):
        for s in range(num1, num2 + 1):
            for r in range(num1, num2 + 1):
                if (i % 2 == 0 and r % 2 != 0 or i % 2 != 0 and r % 2 == 0) and i > r and (n + s) % 2 == 0:
                    print(f'{i}{n}{s}{r}', end=' ')
