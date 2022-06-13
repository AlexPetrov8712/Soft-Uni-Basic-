n = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
sums = 0
for i in range(0, n):
    grams_cat = int(input())
    if 99 < grams_cat < 200:
        group_1 += 1
    elif 199 < grams_cat < 300:
        group_2 += 1
    elif 300 <= grams_cat < 400:
        group_3 += 1
    sums += grams_cat
sums /= 1000
print(f'Group 1: {group_1}')
print(f'Group 2: {group_2}')
print(f'Group 3: {group_3}')
print(f'{sums * 12.45:.2f} lv.')
