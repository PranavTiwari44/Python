str1 = "acegikmoqsuwy"
str2 = "bdfhjlnprtvxz"

merged_Str = ""
for i in range(0, 14):
    if i <= 13:
        if i == 13:
            print("The sorted string is " + merged_Str)
            break
        merged_Str = merged_Str + str1[i] + str2[i]

    else:
        print("Error")
