from termcolor import colored

vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}


while True:
    print("Welcome to CRUD of a car's dictionary: ")
    print("1, Create an entry")
    print("2, Read an entry")
    print("3, Update an entry")
    print("4, Delete an entry")
    print("0, Exit")
    choice = int(input("Please choose here: "))

    if choice == 1:
        entry_create = input("Enter a key and value || separate them by a comma(,): ")
        entry_create_spc = entry_create.split(",")
        vehicles[entry_create_spc[0]] = entry_create_spc[1]
        print("The entry was added!")
        for key in vehicles:
            print(key, vehicles[key], sep=",")

    elif choice == 2:
        entry_read = input("Enter a key to find the value: ")
        print(vehicles[entry_read])

    elif choice == 3:
        entry_update = input("Enter a key and value to update the pre-existing value || separate them by a comma(,): ")
        entry_update_spc = entry_update.split(",")
        vehicles[entry_update_spc[0]] = entry_update_spc[1]
        print("The entry was updated!")
        for key in vehicles:
            print(key, vehicles[key], sep=",")

    elif choice == 4:
        entry_del = input("Enter a key to find the value: ")
        del vehicles[entry_del]
        print("The entry was deleted!")
        for key in vehicles:
            print(key, vehicles[key], sep=",")

    elif choice == 0:
        print(colored("Thank you using our dataservices! ", 'green'))
        break

    else:
        print(colored("Please input appropriate value as per menu", 'red'))
        continue
