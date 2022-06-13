n = int(input())
red = 0
orange = 0
blue = 0
green = 0
most_egg = 0
for i in range(n):
    color = input()
    if color == 'red':
        red += 1
    elif color == 'orange':
        orange += 1
    elif color == 'blue':
        blue += 1
    elif color == 'green':
        green += 1
print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
if red > orange and red > blue and red > green:
    most_egg = red
    color = 'red'
elif orange > red and orange > blue and orange > green:
    most_egg = orange
    color = 'orange'
elif blue > red and blue > orange and blue > green:
    most_egg = blue
    color = 'blue'
elif green > red and green > orange and green > blue:
    most_egg = green
    color = 'green'
print(f'Max eggs: {most_egg} -> {color}')