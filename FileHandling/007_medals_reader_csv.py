"""
    CSV (Comma Separated Values)
        -> The basic idea is that each value on a row is separated form the preceding and following values, with a comma
        -> CSV files are commonly used to export data from one spreadsheet program, to import it into another
        spreadsheet, or a database.
        -> Surprisingly, although CSV files have been used for nearly 50 years, there's no standard definition of CSV.
        -> The closest thing we've found to a standard, is the `Internet Engineering Task Force (IETF) RFC 4180`
        -> RFC is a `Request for Comments`, and these documents form the basis for standards on the internet.
        But RFC 4180 doesn't define a standard for CSV files.

        -> A CSV file contains rows of data, with each row having the same number of "fields". Each field is separated
        by some character. That can be comma, but you can also use tabs or spaces, or any other character that's
        appropriate.

"""

import csv

csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')
    print(f'Column headers: {headers}')
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
