import sys
unsorted_Data = []
try:
    data = sorted(unsorted_Data)

    min_valid = 100
    max_valid = 200

    stop = 0

    for index, value in enumerate(data):
        if value >= min_valid:
            stop = index
            break

    print(stop)
    del data[:stop]
    print(data)

    start = 0

    for index in range(len(data) - 1, -1, -1):
        if data[index] <= max_valid:
            start = index+1
            break

    print(start)
    del data[start:]
    print(data)

except IndexError:
    print("The provided list has no data, Add date!")
    sys.exit(1)

