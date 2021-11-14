import pandas
initialSample = "This past summer, I had the privilege of participating in the University of Notre Dame's Research Experience for Undergraduates (REU) program ."
str = ""

for characters in initialSample:
    if " " not in characters:
        if "," not in characters:
            if "'" not in characters:
                if "." not in characters:
                    if "(" not in characters:
                        if ")" not in characters:
                            str = str + characters


print(pandas.Series(list(str.casefold())).value_counts())






