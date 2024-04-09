import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    sample = countries_data.read()
    country_dialect = csv.Sniffer().sniff(sample)
    countries_data.seek(0)  # setting the file ptr to beg of file as in line 6, read() method place it to the end.
    # country_reader = csv.reader(countries_data, delimiter='|')
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)


"""
    seek():
        The seek method is used to position the file pointer to another place in file. 
        
    The above code is not efficient with large number of data in file. Sniffer needs only a sample of the data.
    Generally, two or three lines should be sufficient.
    We will use 3 lines as a sample for sniff() method
"""
