choice = 10

while choice != 0:
    print("1. Learn python")
    print("2. Tech python")
    print("3. Make an assignment in python")
    print("4. Make an assignment in python")
    print("0. Exit")
    choice = int(input("please enter your choice: "))

    if choice != 0 and choice < 5:
        print("You selected this {} option".format(choice))
        break
    elif choice not in (1,2,3,4,0):
        print("Please choose from the following: ")
        continue
else:
    print("Thanks for your time, Have a great day")

