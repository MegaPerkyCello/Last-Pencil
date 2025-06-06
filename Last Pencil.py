import string
import random

while (True):
    try:
        n_pencils = int(input("How many pencils would you like to use:\n"))
    except ValueError:
        print("The number of pencils should be numeric")
    else:
        if n_pencils == 0:
            print("The number of pencils should be positive")
        elif n_pencils < 0:
            print("The number of pencils should be numeric")
        else:
            break

while (True):
    going_first = str(input("Who will be the first (John, Jack):\n"))
    if going_first != "John" and going_first != "Jack":
        print("Choose between 'John' and 'Jack'")
    else:
        going_second = ""
        if going_first == "Jack":
            going_second = "John"
        else:
            going_second = "Jack"
        break
print("|" * n_pencils)

turn = 0
while (True):
    if turn % 2 == 0 and going_first == "John":
        print(f"{going_first}'s turn:")
    elif turn % 2 == 0 and going_first == "Jack":
        print(f"{going_first}'s turn!")
    elif turn % 2 == 1 and going_second == "John":
        print(f"{going_second}'s turn:")
    else:
        print(f"{going_second}'s turn!")

    if turn % 2 == 0 and going_first == "John" or turn % 2 == 1 and going_second == "John":
        while (True):
            try:
                n_take_away = int(input())
            except ValueError:
                print("Possible values: '1', '2' or '3'")
            else:
                if n_take_away > 3 or n_take_away < 1:
                    print("Possible values: '1', '2' or '3'")
                elif n_pencils - n_take_away < 0:
                    print("Too many pencils were taken")
                else:
                    break

        n_pencils -= n_take_away
        if n_pencils == 0:
            if turn % 2 == 0:
                print(f"{going_second} won!")
            else:
                print(f"{going_first} won!")
            break
        else:
            print("|" * n_pencils)
            turn += 1
    else:
        if n_pencils % 4 == 1 and n_pencils != 1:
            n_take_away = random.randint(1, 3)
        elif n_pencils == 1:
            n_take_away = 1

        elif n_pencils % 4 == 0:
            n_take_away = 3
        elif n_pencils % 4 == 3:
            n_take_away = 2
        elif n_pencils % 4 == 2:
            n_take_away = 1

        print(n_take_away)
        n_pencils -= n_take_away
        if n_pencils == 0:
            if turn % 2 == 0:
                print(f"{going_second} won!")
            else:
                print(f"{going_first} won!")
            break
        else:
            print("|" * n_pencils)
            turn += 1





