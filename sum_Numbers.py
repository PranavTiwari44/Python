def sum_numbers(*args: float) -> float:
    """
    This function get as many arguments does an user want to use in function and gives a sum

    :param number: N number of int arguments
    :return: Sum of all the inputted arguments
    """
    sum_number = 0
    for x in args:
        sum_number = sum_number + x
    return sum_number


print(sum_numbers(12.5, 3.147, 98.1))
