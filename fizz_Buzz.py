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


for number in range(lowest, highest+1):
    print(fizz_buzz(number))
