minutes_walk_day = int(input())
number_walk_day = int(input())
calories_per_dey = int(input())
all_walk = minutes_walk_day * number_walk_day
all_calories = all_walk * 5
half_calories = calories_per_dey * (50 / 100)
if all_calories >= half_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {all_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {all_calories}.')