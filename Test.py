#print("Pepe")
#print("The student name is {0}".format("pranav"))

#for i in range(1, 11):
#    if i < 11:
#        {print("No. {0:2} squared is {1:3}".format(i, i ** 2))}

#print("\n")
#print("Pi is {0:.50f}".format(22/7))

#centerString = "center"
#print((centerString.center(100)).count(" "))


#import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
#left = [1, 2, 3, 4, 5]

# heights of bars
#height = [10, 24, 36, 40, 5]

# labels for bars
#tick_label = ['one', 'two', 'three', 'four', 'five']

# plotting a bar chart
#plt.bar(left, height, tick_label = tick_label,
#        width = 0.8, color = ['red', 'green'])

# naming the x-axis
#plt.xlabel('x - axis')
# naming the y-axis
#plt.ylabel('y - axis')
# plot title
#plt.title('My bar chart!')

# function to show the plot
#plt.show()

#import pandas
#import re

#initialSample = "This past summer, I had the privilege of participating in the University of Notre Dame's Research Experience for Undergraduates (REU) program ."
#strF = ""
#str = re.sub(r"[^a-zA-Z0-9]","",initialSample)

#for characters in str:
#        strF = str + characters


#print(pandas.Series(list(strF.casefold())).get(0))
#initialSample = "This past summer, I had the privilege of participating in the University of Notre Dame's Research Experience for Undergraduates (REU) program ."

#ords = initialSample.split() #read the words into a list.
#uniqWords = set(words) #remove duplicate words and sort
#for word in uniqWords:
#       word.sort(key = lambda x: (words[x]["word"], words[x]["words.count(word)"]))
#        print(word)
data = [
        "Andromeda - Shrub",
        "Bellflower - Flower",
        "China Pink - Flower",
        "Daffodil - Flower",
        "Evening Primrose - Flower",
        "French Marigold - Flower",
        "Hydrangea - Shrub",
        "Iris - Flower",
        "Japanese Camellia - Shrub",
        "Lavender - Shrub",
        "Lilac - Shrub",
        "Magnolia - Shrub",
        "Peony - Shrub",
        "Queen Anne's Lace - Flower",
        "Red Hot Poker - Flower",
        "Snapdragon - Flower",
        "Sunflower - Flower",
        "Tiger Lily - Flower",
        "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

for dt in data[:]:
        if "- Flower" in dt:
                flowers.append(dt.replace("- Flower", ""))
        else:
                shrubs.append(dt.replace("- Shrub", ""))

print(flowers)
print(shrubs)

flowers.extend(shrubs)
print(flowers[11])