import pandas
initialSample = "This past summer, I had the privilege of participating in the University of Notre Dame's Research Experience for Undergraduates (REU) program ."
str = ""

for characters in initialSample:
        if "," not in characters:
            if "'" not in characters:
                if "." not in characters:
                    if "(" not in characters:
                        if ")" not in characters:
                            str = str + characters

data = str.split()
print(pandas.Series(list(data)).value_counts())
