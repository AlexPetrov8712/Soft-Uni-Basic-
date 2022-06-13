command = input()
adults = 0
kids = 0

while command != "Christmas":
    years = int(command)

    if years <= 16:
        kids += 1
    else:
        adults += 1

    command = input()

kidsPrice = kids * 5
adultsPrice = adults * 15

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {kidsPrice}")
print(f"Money for sweaters: {adultsPrice}")
