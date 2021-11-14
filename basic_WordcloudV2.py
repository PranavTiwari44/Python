import pandas
import re
initialSample = "This past summer, I had the privilege of participating in the University of Notre Dame's Research Experience for Undergraduates (REU) program ."

str = re.sub(r"[^a-zA-Z0-9 ]","",initialSample)

data = str.split()
print(pandas.Series(list(data)).value_counts())
