from contents import recipes


def deep_copy(d: dict) -> dict:
    copied_dict = {}
    for keys, value in d.items():
        new_values = value.copy()
        copied_dict[keys] = new_values
    return copied_dict


recipy_copy = deep_copy(recipes)
recipy_copy["Butter chicken"]["ginger"] = 300
print(recipy_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])

