import random

highest = 20
answer = random.randint(1, highest)


def get_integer(stmnt):
    while True:
        number = input(stmnt)
        if number.isnumeric():
            return int(number)
        print("{} is not a valid number".format(number))


def guessing(numb):
    while numb != answer:
        numb = get_integer("Guess here again: ")
        if numb == answer:
            continue
        else:
            if numb < answer:
                print("Guess Higher Please!")
            else:
                print("Guess Lower Please!")
    print("You got it!")


guess = int(input("Guess a number between 1 - {}: ".format(highest)))
guessing(guess)
