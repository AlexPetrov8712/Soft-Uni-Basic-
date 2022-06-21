bakers_num = int(input())
won_baker = ''
max_point = 0
for i in range(bakers_num):
    baker_name = input()
    current_point = 0
    while True:
        info = input()
        if info == 'Stop':
            break
        current_point += int(info)
    print(f"{baker_name} has {current_point} points.")
    if current_point > max_point:
        max_point = current_point
        won_baker = baker_name
        print(f"{baker_name} is the new number 1!")
print(f"{won_baker} won competition with {max_point} points!")

