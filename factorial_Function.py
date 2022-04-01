lowest = 0
highest = 35


def factorial(num: int) -> int:
    """
    This function calculates the factorial of the number provided

    :param num: The function will receive an integer
    :return: The function will return an integer as well
    """
    fact = 1
    if num == 0:
        return 1
    else:
        for i in range(1, num+1):
            fact = fact * i
        return fact


for number in range(lowest, highest+1):
    print("{} {}".format(number, factorial(number)))
