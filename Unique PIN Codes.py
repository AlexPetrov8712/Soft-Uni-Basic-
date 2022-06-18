number1 = int(input())
number2 = int(input())
number3 = int(input())
for num1 in range(1, number1 + 1):
    for num2 in range(2, number2):
        for num3 in range(1, number3 + 1):
            if num1 % 2 == 0 and num3 % 2 == 0:
                if number2 % num2 == 0:
                    print(f'{str(num1)} {str(num2)} {str(num3)}')
