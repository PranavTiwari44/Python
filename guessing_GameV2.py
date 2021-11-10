answer = 5


def guessingsys(numb):
    if numb < answer:
        print("Guess a higher number please!")
        s_guess = int(input("Guess here again: "))
        while s_guess != answer:
            print("Guess a higher number please!")
            s_guess = int(input("Guess here again: "))
        print("You got it!")
    elif numb > answer:
        print("Guess a lower number please!")
        s_guess = int(input("Guess here again: "))
        while s_guess != answer:
            print("Guess a lower number please!")
            s_guess = int(input("Guess here again: "))
        print("You got it!")
    else:
        print("You got it!")


guess = int(input("Guess a number between 1 -  10: "))
guessingsys(guess)





