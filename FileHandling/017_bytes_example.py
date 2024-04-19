'''
    bytes and bytearray (bytes like objects):
        -> bytearray is a mutable version of bytes.
        -> bytes is immutable.
        -> arrays: 
            -> An array is a sequence of numbers
            -> Working with arrays is similar to working with lists, and they're indexed in the same way. Unlike
            lists, which are intended to be homogeneous, this is enforced with arrays. You can't mix strings and
            numbers in the same array.
        
        -> Bytes:
            -> The bytes data type is an array of bytes. So it's an sequence that can store values in the range
            0 to 255.
                index: 0    1   2   3   4   5   6
                value: 112  121 116 104 111 110 45

            -> Unlike array, which has to be imported, the bytes type is built in python.
            -> Each value in a bytes-like object must be a number between 0 and 255.
            -> A `byte` is a sequence of 8 binary digits, which are called `bits`. 8 bits can represent a value
            from 0 to 255.
                00000000 -> 0
                11111111 -> 255
            
            -> Python 3's bytes is the equivalent of the str type, in Python 2.
            -> Python 3's str type is what you'd get in Python 2, if you prefixed a string with 'u'.

                Python 3                                              Python 2
                'This is a unicode string (type str)'   u'This is a unicode string in Python 2'
                b'This is a byte array'                 'This is an array of bytes in Python 2. Its type is str'

        -> byte-like objects:
            bytes and bytearray objects are often used to store Unicode data, so Python provides a way to create
            a bytes object using familiar string syntax.

            The main differences are that we prefix the string with the letter `b`, and we can use hexadecimal
            values for individual bytes.        

            \x escape sequence tells python that what follows will be a hexadecimal value.
            Note that we don't have to use hexadecimal. We can use ASCII characters, and Python will replace
            the character with the ASCII code for that char.
            ASCII code for lowercase letter 'r' is 114 in decimal, or 72 in hex.

        -> Text files are a special case

            There's really no such things as a text file, as far as the computer is concerned. 
            We can read the text in a file, because our editor decodes it and presents the appropriate
            characters on the screen.

            Python performs that decoding for us, if we specify text mode, when we open the file. 
            Python also splits the bytes up at each newline character.

        Unicode is just binary data:
            So all files really contain binary data, but text files are treated differently when specify
            text mode.

            If you wanted to open a text file in binary mode, you can. You'd need to split the data up at
            the newlines, and decode the binary data yourself, but it would work.
'''

# equation = bytes((207, 128, 114, 194, 178))
equation = b'\xcf\x80r\xc2\xb2'  # bytes object (array of bytes - an array of 8 bit numbers)
print(equation)
print(type(equation))
print(len(equation))

for b in equation:
    print(b, end=' ')
print()

print(equation.decode('utf-8'))