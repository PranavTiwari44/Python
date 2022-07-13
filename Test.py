#print("Pepe")
#print("The student _name is {0}".format("pranav"))

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

#words = initialSample.split() #read the words into a list.
#uniqWords = set(words) #remove duplicate words and sort
#for word in uniqWords:
#        word.sort(key = lambda x: (words[x]["word"], words[x]["words.count(word)"]))
#        print(word)

#user_Input = input("Please enter three numbers: ")
#onechar = user_Input.split(",")

#equation = int(onechar[0])+int(onechar[1])-int(onechar[2])
#print(equation)

#import re
#your_string = "hello  my !@#$%^&*()_+}{|:?>< pranav tiwarir ?"
#print(re.sub(r'\W+', '', your_string))

#n=10
#t='e'


#def sum_eo(n, t):
#    """
#    This function gives sum of odd or even number based on user's request

#    :param n: `int` > A number until where the user need the sum for.
#    :param t: `string` > A character based choice to find either even or odd
#   :return:  `int` > Total sum of either the even or odd numbers
#    """
#    if t == 'e':
#       total = 0
#        for sum_e in range(0, n, 2):
#            total = total+sum_e
#        return total
#    elif t == 'o':
#        total = 0
#        for sum_e in range(1, n, 2):
#            total = total+sum_e
#        return total
#    else:
#        return -1


#print(sum_eo(n,t))

# red = '\u001b[31m'
#
# print(red, "this will be in red")

# def star_args(args):
#     for x in args:
#         print(x)
#
#
# string = "hello", "hello1", "hello2", "hello3"
# star_args(string)

# vehicles = {'jumper': 'ford mustang gt500'}
#
# my_car = vehicles['jumper']
# print(my_car)
# vehicles = {
#     'dream': 'Honda 250T',
#     'roadster': 'BMW R1100',
#     'er5': 'Kawasaki ER5',
#     'can-am': 'Bombardier Can-Am 250',
#     'virago': 'Yamaha XV250',
#     'tenere': 'Yamaha XT650',
#     'jimny': 'Suzuki Jimny 1.5',
#     'fiesta': 'Ford Fiesta Ghia 1.4',
# }
#
#
# vehicles['gordan'] = "G class"
# for key, value in vehicles.items():
#     print(key, value, sep=",")

# We need an empty dictionary, to store and display the letter frequencies.