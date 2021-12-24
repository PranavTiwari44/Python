import random

highest = 20
answer = random.randint(1, highest)

def guessing(numb):
    while numb != answer:
        numb = int(input("Guess here again: "))
        if numb == answer:
            continue
        else:
            if numb < answer:
                print("Guess Higher Please!")
            else:
                print("Guess Lower Please!")
    print("You got it!")

guess = int(input("Guess a number between 1 -  {}: ".format(highest)))
guessing(guess)
