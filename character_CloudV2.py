import pandas
import re

initialSample = "This past summer, I had the privilege of participating in the University of Notre Dame's Research Experience for Undergraduates (REU) program ."
strF = ""
str = re.sub(r"[^a-zA-Z0-9]","",initialSample)

for characters in str:
    strF = str + characters


print(pandas.Series(list(strF.casefold())).value_counts())