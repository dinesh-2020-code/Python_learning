input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip().split('|')  # strip() method will remove trailing '\n' whitespace char
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
        # print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

# print(countries)
while True:
    country_name = input("Enter country name or code: ")
    country_key = country_name.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(country_data)
        country_capital = country_data['capital']
        print(f"The capital of '{country_name}' is '{country_capital}'")
    elif country_name == 'quit':
        break
    else:
        print(f"'{country_name}' not exists in list")
