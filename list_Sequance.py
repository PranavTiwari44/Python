colorsList = ["Yellow", "green", "black", "orange", "blue"]

for colors in colorsList[0:4:2]:
    if "green" in colors:
        continue
    print(colors)

