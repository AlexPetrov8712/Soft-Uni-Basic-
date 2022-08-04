price_per_kilogram_of_vegetables = float(input())
price_per_kilogram_of_fruit = float(input())
total_of_vegetables = float(input())
total_of_fruit = float(input())
total_veg = price_per_kilogram_of_vegetables * total_of_vegetables
total_fru = price_per_kilogram_of_fruit * total_of_fruit
total_f = total_fru / 1.94
total_v = total_veg / 1.94
total = total_f + total_v
print('%.2f' % total)
 