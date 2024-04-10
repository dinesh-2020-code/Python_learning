import csv

country_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'

countries = {}

with open(country_filename, encoding='utf-8', newline='') as country_file:
    # Get the header from teh first line of the file
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

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
