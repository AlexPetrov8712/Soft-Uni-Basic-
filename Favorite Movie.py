command = ""
movies = 0
max_ASCII = 0
best_movie = ""

while command != "STOP":
    command = input()
    ASCII = 0
    total_ASCII = 0
    movies += 1
    for i in range(len(command)):
        ASCII_converting = ord(command[i])
        if "A" <= command[i] <= "Z":
            ASCII = ASCII_converting - len(command)
        elif "a" <= command[i] <= "z":
            ASCII = ASCII_converting - len(command) * 2
        else:
            ASCII = ASCII_converting
            total_ASCII += ASCII
            if total_ASCII > max_ASCII:
                max_ASCII = total_ASCII
                best_movie = command
            if movies >= 7:
                print("The limit is reached.")
                print(f'The best movie for you is {best_movie} with {max_ASCII} ASCII sum.')
                break
    else:
        print(f'The best movie for you is {best_movie} with {max_ASCII} ASCII sum.')
        break

