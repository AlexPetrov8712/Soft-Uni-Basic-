num_people = int(input())
num_sleep = int(input())
num_card = int(input())
num_museum = int(input())
sums_per_men = num_sleep * 20
sums_card = num_card * 1.60
sums_museum = num_museum * 6
all_sum_per_men = sums_per_men + sums_card + sums_museum
all_sum = all_sum_per_men * num_people
print(f'{all_sum * 1.25:.2f}')