the_file = "country_info.txt"

countries = {}
with open(the_file) as country_file:
    next(country_file)
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        countries[country.casefold()] = country_dict

loop_agr = True
while loop_agr:
    user_choice = input("Enter the country to get to know capital: ").casefold()
    for key, value in countries.items():
        if key == user_choice:
            print(f"The capital of {user_choice} is {value['capital']}")
        elif user_choice == 'quit':
            loop_agr = False
