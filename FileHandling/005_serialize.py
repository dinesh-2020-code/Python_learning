"""
Serialization:
    In computing, serialization (or serialisation) is the process of translating a data structure or object state into a
    format that can be stored (e.g. files in secondary storage devices, data buffers in primary storage devices) or
    transmitted (e.g. data streams over computer networks) and reconstructed later (possibly in a different computer
    environment)

    The whole point of serialising something is so that you can either store it somehow, or send it somewhere else.
    For ex: we've seen that we can't write numbers to a text file.
    Instead, we had to write the individual chars - the digits - that made up the number.
    We took a numerical value, and serialized it into its individual digits

Serialization Standards:
    If serialized data is going to be useful to different programs and computer systems, then it needs to follow a
    well-defined standard. JSON is one such standard.

    The International Standards Organisation (ISO) released the standard `ISO/IEC 21778:2017` in 2017. That standard is
    consistent with the ECMA-404 standard for JSON.

    That means any valid JSON that you create can be read by any standards-compliant JSON parser, anywhere in the world.

    JSON:
        JSON is an open standard (no patent issues) format for saving and interchanging data. JSON is human-readable,
        as numbers, and other objects, are serialized to plain text.
        Applications can include JSON parser, that takes the JSON text, and parses it into a format that the application
        can use. Python includes a `json` module

        When to use JSON?
            -> Use JSON when you want to store data, or transmit it, in a format that other systems can use.
            -> JSON isn't suitable for storing your program's data, if you need to preserve the exact type. As we've
             seen,it can only be used to represent a limited number of data types. Those types are usually sufficient,
             when you're only interested in the actual data. They're not suitable when the exact type of the object is
             important. That's rarely the case, when transferring JSON, but is important if you want to save data in
             your program, and get back exactly what you saved, later.

        Limitations of JSON
            -> The main limitation of JSON is related to the problem we've already seen: JSON only supports seven data
            types.
            In particular, there's no support for things like dates
            The decoding program needs to know how you've stored your dates in strings.
            There is an international standard of storing dates (ISO 8601). When including dates in your JSON data, we
            definitely recommend sticking to one of the formats in that standard.

            Another example is representing complex numbers. The usual way, in JSON, is to use a list. For example
            12.5 + 3i would be stored as [12.5, 3] and it's left to the decoding program to know that a complex number
            is present at that position in the data.

        Why use JSON?
            -> Despite those limitations, JSON has become a popular format on the internet.
            -> It's size is often many times smaller than formats such as XML, for example. That can be important when
            you want a web page to load quickly, without having to wait while a large amount of data is downloaded.
            -> JSON is also easy to parse - in part because of its simplicity. Encoders and decoders are available for
            most programming languages in use today.
            -> It's also very easy to read and edit. Whitespace is unimportant (except inside strings) and it's quite
            hard ot mess up a JSON document by accident.

"""

import json

languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Module-2', 1977),
    ('Perl', 1987),
]

with open('test.json', 'w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)

with open('test.json', 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)

print(data)
