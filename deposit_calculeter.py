deposit_sum = float(input())
months = int(input())
year_gear_percent = float(input()) / 100
month_gain = (deposit_sum * year_gear_percent) / 12
final_sum = deposit_sum + (months * month_gain)

print(final_sum)
