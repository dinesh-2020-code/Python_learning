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
'''

# equation = bytes((207, 128, 114, 194, 178))
equation = b'\xcf\x80r\xc2\xb2'
print(equation)
print(type(equation))
print(len(equation))