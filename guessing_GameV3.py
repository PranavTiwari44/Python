import random

highest = 10
answer = random.randint(1, highest)

def guessing(numb):
    if numb < answer:
        print("Guess a higher number please!")
        s_guess = int(input("Guess here again: "))
        while s_guess != answer:
            print("Try again with a different number please!")
            s_guess = int(input("Guess here again: "))
        print("You got it!")
    elif numb > answer:
        print("Guess a lower number please!")
        s_guess = int(input("Guess here again: "))
        while s_guess != answer:
            print("Try again with a different number please!")
            s_guess = int(input("Guess here again: "))
        print("You got it!")
    else:
        print("You got it!")


guess = int(input("Guess a number between 1 -  10: "))
guessing(guess)
