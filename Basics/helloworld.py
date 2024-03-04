print('hello world!')

# print("Python's strings are easy to use.")

# name = input("Please enter your name: ")
# print("hello" + ' ' + name)

"""

In python all functions return the value.


Variables and Types: 
    When a program's running, everything the program needs ends up stored in the computer's memory. The program
    code itself will be stored in one area of memory, and the data it works on will also be stored somewhere in 
    the memory. 
    
    A variable is basically just a way to give a name to an area of memory, into which we can place certain values.
        Variables are created when they are first bound to a value, using =.

    defining a variable means to bind the value to a variable of specific type


    Python Data Types
        -> numeric
        -> iterator
        -> sequence (which are also iterators)
        -> mapping
        -> file
        -> class
        -> exception

    Numeric Data Types
        Python3 has three numeric data types:
            -> int
            -> float
            -> complex

        Python2 had another type 'long', because it's 'int' type couldn't store very large values. In Python3, the 'int' type replaces 'long'

        -> Integer & Float Data Types
            Integers are just whole numbers - numbers having no fractional part; whereas float is
            another name for real numbers - numbers having a fractional part after the decimal point.

            Integers can be considered just special cases of real numbers - but when represented in a computer, computations using integers are 
            significantly faster than using floating point numbers.

            Integers are generally stored in the computer's memory, many programming languages have a limit to the size of an integer - about
            9 trillion in European terms, 9 quintillion in American. Python3 'int' effectively has no max size.


        -> Floating point numbers are used to represent numbers having fractional part.
            The python floating type is called 'float'
            Examples: 1.0, 123.455 etc

            The max float value on a 64-bit computer is 1.7976931348623157e+308 which means move the decimal point 308 places right.
            The smallest float is 2.2250738585072014e-308, which has 307 after the decimal point

            Python floats have 52 digits of precision, which should be adequate for most purposes. If you need more precise decimal numbers, 
            Python3 now includes a 'Decimal' data type.

            because Python doesn't have type declarations(where you specify type of a variable before you can use it), it is tempting to think that you
            don't have to understand the difference between the 'int' and 'float' types.

        
        Expressions: Anything in python that evaluates to some value.
            (2 + 6), (3 * 4) etc
            range(1, a // b) is also an expression (contains 2 more expressions as '1' {evaluates to datatype 'int'}, a // b ) evaluates to range of numbers
            a = 12 // not an expression, rather it's an assignment or we can say value 12 is bound to variable 'a'
            b = 3 // not an expression, rather it's an assignment or we can say value 3 is bound to variable 'b'

            expressions can't come on LHS of '=' operator.
        
        Operator Precedence: which operator will be higher in importance
            BEDMAS: Brackets, Exponents, Division/Multiplication, Addition/Subtraction
            BODMAS: Brackets, Order, Division/Multiplication, Addition/Subtraction

                Division and Multiplication have Equal precedence
                Addition and Subtraction have Equal precedence

                In an expression that mixes operations with equal precedence, they're evaluated from left to right.
        
        String datatypes in Python (str):
            sequence of chars 

        Python Sequence Types: (built-in)
            -> The string type
            -> list
            -> tuple
            -> range
            -> bytes and bytearray

        Sequence: ordered set of items
            for ex: string "Hello World" contains 11 items, and each of item is a character

            -> Not all sequence types can be concatenated or multiplied. 'range' is an example of a sequence that can't be concatenated



""" 


# greeting = 'hello'
# print(greeting)
# print(type(greeting))

# greeting = 2
# print(greeting)
# print(type(greeting))

# name = 'Aman'
# age = 21
# print(name + ' is ' + age + " years old")  # error: TypeError: can only concatenate str (not "int") to str


