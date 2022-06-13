import math

number = int(input())
sugar = 0
flour = 0
max_sugar = 0
max_flour = 0
for i in range(number):
    sugar_grams = int(input())
    flour_grams = int(input())
    sugar += sugar_grams
    flour += flour_grams
    if sugar_grams > max_sugar:
        max_sugar = sugar_grams
    if flour_grams > max_flour:
        max_flour = flour_grams
sugar_need = math.ceil(sugar / 950)
flour_need = math.ceil(flour / 750)
print(f'Sugar: {sugar_need}')
print(f'Flour: {flour_need}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')

