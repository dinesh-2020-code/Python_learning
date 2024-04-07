data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_filename = "flowers_print.txt"
#
# with open(plants_filename, 'w') as plants:
#     for plant in data:
#         print(plant, file=plants)
#
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
#
# print(new_list)

'''
    __str__ method():
    The print() function calls this special method, that all objects have, before printing the object.
    This method returns a string representation of the object. That's what allows `print` to print objects to the screen
    
    Difference between write() and print() when storing text in a file
        The print function will print the string representation of any object that you ask it to print. In addition, it
        will include a separator between multiple arguments - the default is a space, but that can eb changed with the
        `sep` keyword argument.
        Finally, it will print the value of the `end` keyword argument. The default is newline char ('\n)
        
        The `write` method will only write exactly what you tell it to write. 
        No separators or newline characters are included, unless you explicitly tell it to write them. 
        Also no conversion is performed. If you tell `write` to write an integer, that's what it will try to send to the
        file. If the file is opened in text mode (the default), you'll get an error if you try to write numerical
        values to it.
'''
# plants_filename = "flowers_write.txt"
# with open(plants_filename, 'w') as plants:
#     for plant in data:
#         plants.write(plant)
#
# print(data)
# string_representation = data.__str__()
# print(type(string_representation))

filename = "test_numbers.txt"

with open(filename, 'w') as test:
    for i in range(10):
        print(i, file=test)

with open(filename, 'w') as test:
    for i in range(10):
        # test.write(i) # error
        test.write(str(i) + "\n")

