answer = 5

guess = int(input("Guess here: "))

if guess < answer:
    print("Guess a higher number please!")
    s_guess = int(input("Try another number here: "))
    if s_guess < answer:
        print("Guess a higher number please!")
    elif s_guess > answer:
        print("Guess a lower number please!")
    else:
        print("You got it!")
elif guess > answer:
    print("Guess a lower number please!")
    s_guess = int(input("Try another number here: "))
    if s_guess < answer:
        print("Guess a higher number please!")
    elif s_guess > answer:
        print("Guess a lower number please!")
    else:
        print("You got it!")
else:
    print("You got it!")
