number_detergent = int(input())
total_detergent = 750 * number_detergent
number_plate = 0
number_pot = 0
total_plate = 0
total_pot = 0
command = input()
count = 0
total = 0
while command != 'End':
    vessels = int(command)
    count += 1
    if count % 3 == 0:
        number_pot += vessels
        total_pot += vessels * 15
    else:
        number_plate += vessels
        total_plate += vessels * 5
    total = total_plate + total_pot
    if total_detergent < total:
        break
    command = input()
if command == 'End':
    print(f'Detergent was enough!')
    print(f'{number_plate} dishes and {number_pot} pots were washed.')
    print(f'Leftover detergent {total_detergent - total} ml.')
else:
    print(f'Not enough detergent, {abs(total_detergent - total)} ml. more necessary!')
