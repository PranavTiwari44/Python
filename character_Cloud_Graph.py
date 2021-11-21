import pandas
import re
import matplotlib.pyplot as plt

initialSample = "This past summer, I had the privilege of participating in the University of Notre Dame's Research Experience for Undergraduates (REU) program ."
strF = ""
str = re.sub(r"[^a-zA-Z0-9]", "", initialSample)

for characters in str:
    strF = str + characters

str_Final = pandas.Series(list(strF.casefold())).value_counts()

left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# heights of bars
height = str_Final[0:20]

# labels for bars
tick_label = ['E', 'R', 'I', 'T', 'A', 'S', 'P', 'N', 'U', 'H', 'O', 'G', 'D', 'M', 'F', 'C', 'V', 'L', 'Y', 'X']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])

# naming the x-axis
plt.xlabel('Characters')
# naming the y-axis
plt.ylabel('No. of character counts')
# plot title
plt.title('Character cloud!')

# function to show the plot
plt.show()


