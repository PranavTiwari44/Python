import random

highest = 20
answer = random.randint(1, highest)
count = 0

numb = int(input("Guess a number between 1 - {}: ".format(highest)))
while numb != answer:
        numb = int(input("Guess here again: "))
        if numb == answer:
            continue
        else:
            if numb < answer:
                print("Guess Higher Please!")
                count += 1
            else:
                print("Guess Lower Please!")
                count += 1
print("You got it!")
if count >= (highest*0.75):
    print("You scored 25 points out of 100: Better luck next time!")
elif (highest * 0.75) > count >= (highest * 0.5):
    print("You scored 50 points out of 100: You can do better!")
elif (highest * 0.5) > count >= (highest * 0.25):
    print("You scored 75 points out of 100: Good work!")
elif 3 > count:
    print("You scored 100 points out of 100: Awesome!")
