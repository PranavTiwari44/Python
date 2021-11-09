answer = 5

def guessingsys(numb):
    if numb < answer:
        print("Guess a higher number please!")
    elif numb > answer:
        print("Guess a lower number please!")
    else:
        print("You got it!")


guess = int(input("Guess here: "))
while guess == answer:
    guessingsys(guess)





