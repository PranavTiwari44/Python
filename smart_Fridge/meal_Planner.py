from contents import pantry, recipes

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index+1)] = key

shp_list = {}


def shopping_list(data: dict, food: str, quantity: int) -> None:
    # if food in data:
    #     data[food] += quantity
    # else:
    #     data[food] = quantity
    data[food] = data.setdefault(food, 0) + quantity


while True:
    print("Please choose your recipe:")
    print("**************************")
    for key, value in display_dict.items():
        print(f"{key}: {value}")

    choice = input(": ")

    if choice == '0':
        print("\nThanks for using our meal planner! ")
        break

    elif choice in display_dict:
        print("\nThe recipe's ingredients are: ")
        ingredients = recipes[display_dict[choice]]
        for index, value in enumerate(ingredients):
            print(f"{index+1}: {value}")
        print("\n")
        print("Checking pantry for availability of the ingredients!\n")
        for available_food, req_quantity in ingredients.items():
            if available_food in pantry:
                print(f"{available_food} OK")
                if req_quantity <= pantry[available_food]:
                    print(f"After making this dish, you will have {pantry[available_food]-req_quantity} "
                          f"{available_food} left!")
                else:
                    print(f"You will need more {req_quantity-pantry[available_food]} {available_food} "
                          f"to make this dish!")
                    shopping_list(shp_list, available_food, req_quantity-pantry[available_food])
                    print(f"{req_quantity-pantry[available_food]} {available_food} is added to shopping list!\n")
            else:
                print(f"You don't have {available_food} in your pantry!")
                shopping_list(shp_list, available_food, req_quantity)
                print(f"{req_quantity} {available_food} is added to shopping list!\n")

        print("\n")
        print("The shopping list have these things to buy: ")
        for name, value in sorted(shp_list.items()):
            print(f"{name}: {value}")
        print("\n")

    else:
        print("\nPlease choose from the following menu options!")
        continue
