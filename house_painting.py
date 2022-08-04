x = float(input())
y = float(input())
h = float(input())
front_rear_side = (x * x) * 2
the_side_walls = (x * y) * 2
windows = 4.5
door = 2.4
total_front_rear_side = front_rear_side - door
total_side_walls = the_side_walls - windows
roof_one = x * y * 2
roof_two = (x * h / 2) * 2
roof_total = roof_one + roof_two
all_green = (total_side_walls + total_front_rear_side) / 3.4
all_red = roof_total / 4.3
print('%.2f' % all_green)
print('%.2f' % all_red)
