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
                
            Unicode: 
                ASCII: 
                    A long long time ago, when the world was young, characters were encoded using a single byte for each
                    character. A byte is 8 bits, and can represent decimal numbers from 0 to 255. That meant a maximum 
                    of 256 chars could be represented.
                    
                    There were 2 different encodings in common use: 
                        IBM mainframes used EBCDIC (pronounced ebb-sid-ick). They still do today.
                        As personal computers developed, they used ASCII. 
                    
                        ASCII is a 7-bit code - so it could only represent 127 different chars. ASCII became the most 
                        popular encoding on PCs and smaller computers, and you'll still hear programmers referring to
                        ASCII when talking about encoding characters. 
                        Despite only being able to represent 127 chars and control codes, ASCII was suitable for the
                        computations needs of the time.
                        
                        But times have changed. Even the visionaries of the past couldn't predict just how much things
                        would change. 
                        Thomas J. Watson, the founder of IBM said: 
                            "I think there is a world for maybe five computers."
                        
                        MS-DOS, teh operating system that the first versions of Windows ran on, was restricted to 640KBs
                        of addressable memory, Bill Gates said:
                            "640K of memory should be enough for everyone."
                        
                        ASCII was fine for representing the Latin alphabet used in the English language, but couldn't
                        represent characters with accents. That means ASCII couldn't represent all the characters in
                        languages that use the Latin alphabet, but also include diacritics (accents). 
                        
                        All modern European languages, except English, commonly use diacritics. Any language that didn't
                        use the Latin alphabet couldn't be represented at all. 
                        So most of the world couldn't use a computer in their native language.
                        
                    Technical Debt: 
                        It is a term used to describe problems that we face, because of decisions made in the past. 
                        It also describes problems that we're creating for the future, if we choose limited solutions
                        now. 
                        Google engineers suffered with technical debt for several years, as they continued supporting
                        older versions of the Android mobile phone operating system. In 2019, they stopped  Android 
                        versions from 2011 and earlier.
                        The latest of those versions was only 8 years old, but the difficulty of continuing to support 
                        it was restricting the future development of later versions. 
                        
                        The adoption of ASCII led to technical debt. With a maximum of 127 chars, it wasn't suitable for
                        representing accents, nor the different scripts - Chinese, Japanese, Cyrillic, Arabic, and so on
                        - that are used throughout the world.
                        
                        But dropping support for ASCII enoded files wasn't an option. ASCII was used to represent text
                        in about 27 years worth of files. 
                        
                        Any replacement encoding hard to work for all the existing ASCII files out there, and with all
                        the programs that were continuing to crete ASCII output.
                        
                        Microsoft and IBM each produced their own encodings to support various languages. Some of their
                        encodings were similar, but not exactly the same.  
                        
                    Unicode: 
                        The unicode standard attempts to provide encodings to cater for all the languages in use world-
                        wide. Currently it supports most of them, with more being added. 
                        
                        When the IBM documentation  referred ot Unicode being the preferred character set for the
                        internet, it's referring to `Unicode Transformation Format - 8 bit` or `UTF-8`.
                        
                        Python generally uses UTF-8 by default, on many systems. But when you read that, in the Python
                        documentation, it can give you wrong impression. 
                        On windows, in particular, the open() method generally doesn't default to UTF-8
                        
                    Unicode in Python
                        In python 2, you had to explicitly specify that a string is encoded using one of the encodings
                        specified in unicode standard. you had to prefix the string with the letter "u", to create a
                        Unicode string. In python 3, all strings are unicode.
                        
                    CRLF: On windows, a newline is represented by two characters: a carriage return followed by a
                        line feed.
                        On Mac and Linux computers, a single line feed character is used instead. If you're using Linux
                        or a Mac, you should see LF there, in place of CRLF that Windows computer is using.
                    
                    File encodings: 
                        -> ISO-8859-1: ISO-8859-1 was the basis for the first 256 Unicode code points. These are all 
                        single-byte representations of characters, with the first 127 matching the ASCII chars.
                        It includes most of the accenetd characters in use in Western European languages.
                            
                            Code Point: It refers to the individual codes that are defined to represent chars
                                As we've seen, ASCII can represent 127 different chars. Note that we don't count zero in
                                that range. 
                                The code point `65` represents a capital letter `A`.
                                The first 32 code points are control codes - things like 9 for a tab, 10 for a line feed
                                , and 13 for a carriage return.
                                Back then, they were called `ASCII codes` rather than code points. But when dealing with
                                more modern encodings, we talk about `code points` instead.
                                
                                When dealing with code points, note that they're not restricted to single-byte values.
                                If they were, we'd still be stuck with only 256 possible codes.
                                Instead, a code point can be 1 or more bytes. 
                                
                        -> UTF-8: for example, uses 1 byte for the first 128 characters, which corresponds to the
                            ASCII character set.
                            The next 1,920 chars are represented by 2 bytes. 
                            Following on, and using 3 bytes each, are mostg of the Chinese, Japanese and Korean
                            chars. Lesser used CJK(Chinese, Japanese, Korean) chars, mathematical symbols, musical
                            characters and emojis are encoded using 4 bytes each.
                                
                        -> UTF-16: 
                            UTF-16 is a unicode transformation format that uses one or two 16 bit codes. It was
                            adopted by Microsoft, but since 2019 Windows switched to UTF-8.
                            
                            If the smallest size of a code point is 2 bytes (16 bits), a file using only the Latin
                            alphabet will be twice as large as the same text encoded with UTF-8.
                            That's one reason why UTF-16 has fallen out of favour.
                        
                        -> windows-1252:
                            windows-1252 is a single-byte encoding adopted by Microsoft. It's basically ISO-8859-1 with
                            some extra characters.
                            
                            It's important, because that's the encoding that Python will most likely choose, when you 
                            call open function on windows.
                            Of course, this is only true if your windows setup is using the Latin alphabet. If you're
                            using a different alphabet for your language, the Windows file system will use a suitable
                            encoding, and that will be the default encoding used by open().
                            
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

