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
        
        File Modes: 
            'r': open for reading (default)
            'w': open for writing, truncating the file first
            'x': open for exclusive creation, failing if the file already exists
            'a': open for writing, appending to the end of the file it it exists
            'b': binary mode
            't': text mode (default)
            '+': open for updating (reading and writing)
        
        Buffer (or cache)
            -> Because disk drives are slow - compared to computer memory, they're very slow - data is read in large chunks
                into an area of memory called a "buffer".
            -> That makes the data available when you want to read more data, without having to wait for the disk drive to 
                spin around again. 
            -> Of course, if you're using modern SSD drives, they don't spin. But they're still a lot slower that your
                computer's memory. 
            -> By reading larger chunks from the drive, the next data that you'll probably want is made available faster. 
                A disk buffer is also called a `disk cache`.
            -> When writing data to disk, the data is put into a buffer first. 
                That allows your program to move on, without waiting for the actual transfer to complete.
                The write to disk can happen in the background, while your code gets on with other things.
                That's another reason why it's very important to always close a file, when writing. 
                If you fail to close the file, and your program terminates, data in teh cache might not be written to
                the disk - resulting in data loss.
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

