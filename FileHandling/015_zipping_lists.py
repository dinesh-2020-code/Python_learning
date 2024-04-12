'''
    The zip() function: 
        -> Takes iterables and returns an iterable containing tuples. If you provide two lists,
        for example, each tuple will contain two items - one from each list, in turn.

'''
import csv

albums_data = [("Welcome to my Nightmare", "Alice Cooper", 1975),
               ("Bad Company", "Bad Company", 1974),
               ("Nightflight", "Budgie", 1981),
               ("More Mayhem", "Imelda May", 2011),
               ("Ride the Lightening", "Metallica", 1984),
               ]

keys = ['album', 'artist', 'year']

filename = 'albums.csv'

with open(filename, 'w', encoding='utf8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys, quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for row in albums_data:
        # print(row)
        zip_object = zip(keys, row)
        # print(zip_object)
        # for thing in zip(keys, row):
        #     print(f"\t{thing}")
        albums_dict = dict(zip_object)
        # print(albums_dict)
        writer.writerow(albums_dict)

