num = int(input())
is_break = False

for a in range(1, 9):
    for b in range(9, a, -1):
        for c in range(9):
            for d in range(9, c, -1):
                if (a + b + c + d) == a * b * c * d and num % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    is_break = True
                    exit()

                elif a * b * c * d // (a + b + c + d) == 3 and num % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    is_break = True
                    exit()
if not is_break:
    print("Nothing found")