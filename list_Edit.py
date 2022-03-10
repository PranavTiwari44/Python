menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for menu_List in menu:
    for index in range(len(menu_List) - 1, -1, -1):
        if menu_List[index] == "spam":
            del menu_List[index]
    print(menu_List)

print("-------------------------------------------------------------------")

for menu_List in menu:
    for menu_Item in menu_List:
        if "spam" not in menu_Item:
            print(menu_Item, end=" ")
    print()