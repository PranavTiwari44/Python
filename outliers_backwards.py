min_valid = 10
max_valid = 997

data = list(range(1000))

for index in range(len(data) - 1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        del data[index]

print(data)
