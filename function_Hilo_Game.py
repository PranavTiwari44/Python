import timeCalc
lowest = 1
highest = 1000


def hilo(answer, low, high):
    guesses = 1
    while True:
        guess = low + (high - low) // 2
        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        elif guess == answer:
            return guesses
        guesses += 1


t0 = time.time()
count = 0
correct = 0
max_count = 0
for number in range(lowest, highest+1):
    number_of_guesses = hilo(number, lowest, highest)
    print("{} you guessed in {}".format(number, number_of_guesses))

    if max_count < number_of_guesses:
        max_count, correct = number_of_guesses, 1
    elif number_of_guesses == max_count:
        correct += 1

print("I guessed correctly for {} times. Max guess is {}".format(correct, max_count))
t1 = time.time()
total = t1 - t0
print(total)
