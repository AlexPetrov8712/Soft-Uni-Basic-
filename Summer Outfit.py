degrees = int(input())
day_time = input()
Outfit = ''
Shoes = ''
if day_time == 'Morning':
    if 10 <= degrees <= 18:
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    elif 18 < degrees <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    else:
        Outfit = 'T - Shirt'
        Shoes = 'Sandals'
if day_time == 'Afternoon':
    if 10 <= degrees <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    else:
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
if day_time == 'Evening':
    if 10 <= degrees <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    else:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
print(f'It\'s {degrees} degrees, get your {Outfit} and {Shoes}.')






