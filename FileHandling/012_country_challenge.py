import csv

country_filename = 'country_info.txt'

countries = {}

with open(country_filename, encoding='utf-8', newline='') as country_file:
    reader = csv.DictReader(country_file, delimiter='|')
    for row in reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row

# print(countries)

while True:
    country_name = input("Enter country name or code: ")
    country_key = country_name.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(country_data)
        country_capital = country_data['Capital']
        print(f"The capital of '{country_name}' is '{country_capital}'")
    elif country_name == 'quit':
        break
    else:
        print(f"'{country_name}' not exists in list")
