n = int(input())
count = 1
if_count_big_n = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if count > n:
            if_count_big_n = True
            break
        print(str(count) + ' ', end='')
        count += 1
    if if_count_big_n:
        break
    print()

