length = int(input())
width = int(input())
height = int(input())
percent = int(input())
aquarium_volume = length * width * height * 0.001
percent_calc = percent * 0.01
needed_liters = aquarium_volume * (1 - percent_calc)

print(needed_liters)
