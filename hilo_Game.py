import random
lowest = 1
highest = 1000
answer = random.randint(lowest, highest)
print("Please think of a number in {} and {}".format(lowest, highest))
input("Press ENTER to start the game")
guesses = 1

while True:
    guess = lowest + (highest - lowest) // 2
    response = input("My guess is {} || If my guess is lower type : h "
                           "|| If my guess is hi    gher type : l "
                           "|| if my guess is correct type : c "
                           .format(guess)).casefold()
    if response == "h":
        lowest = guess + 1
    elif response == "l":
        highest = guess - 1
    elif response == "c":
        print("I got it in {} guesses GGEZ!".format(guesses))
        break
    else:
        print("Please enter h ,l ,c : ")
    guesses += 1


