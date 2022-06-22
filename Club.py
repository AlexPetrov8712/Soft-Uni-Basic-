needed_sum = float(input())
drink = input()
profit = 0
while drink != "Party!":
    sums = len(drink) * float(input())
    if sums % 2 == 1:
        sums *= 0.75
    profit += sums
    if profit >= needed_sum:
        break
    drink = input()
if needed_sum > profit:
    print(f'We need {needed_sum - profit:.2f} leva more.')
else:
    print("Target acquired.")
print(f'Club income - {profit:.2f} leva.')