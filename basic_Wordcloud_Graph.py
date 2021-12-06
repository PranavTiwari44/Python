import pandas
import re
import matplotlib.pyplot as plt
initialSample = "This past summer, I had the privilege of participating in the University of Notre Dame's Research Experience for Undergraduates (REU) program ."

str = re.sub(r"[^a-zA-Z0-9 ]","",initialSample)

data = str.split()
str_Final = pandas.Series(list(data)).value_counts()

left = [1, 2, 3, 4]

# heights of bars
height = str_Final[0:4]

# labels for bars
tick_label = ['the', 'of', 'this', 'notre']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green', 'black', 'blue', 'purple'])

# naming the x-axis
plt.xlabel('Words')
# naming the y-axis
plt.ylabel('No. of words counts')
# plot title
plt.title('Word cloud!')

# function to show the plot
plt.show()
