def fibonacci(n):
    n_min1 = 1
    n_min2 = 0

    if 0 <= n <= 1:
        return n

    result = None
    for i in range(n-1):
        result = n_min1 + n_min2
        n_min2 = n_min1
        n_min1 = result

    return result


for i in range(20):
    print(i, fibonacci(i))
