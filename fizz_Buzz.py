lowest = 1
highest = 100


def fizz_buzz(num: int) -> str:
    """
    This function takes a number and outputs a fizz,buzz,fizz_buzz, or the number based on a condition

    :param num: A number
    :return: A string
    """
    if num % 3 == 0 and num % 5 == 0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)


input("Play Fizz Buzz. Press Enter to start!")
print()

nxt_number = 0
while nxt_number < 9:
    nxt_number += 1
    print(fizz_buzz(nxt_number))
    nxt_number += 1
    correct_response = fizz_buzz(nxt_number)
    user_response = input("Your turn kid: ")
    if user_response != correct_response:
        print("You are trash kid!")
        break
else:
    print("Well done kid, you are a tough nut!")
