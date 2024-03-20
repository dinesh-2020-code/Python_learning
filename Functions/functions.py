'''
        
    Functions and Methods
        -> Allow reusability of code.

        Methods: A function that's bound to an instance of a class is called a method.
        print() is a function, but .sort in my_list.sort() is a method
        str.casefold() is also a method.

    Parameters and Arguements
        Parameters: Placeholders for the real values that you'll pass to your function
        They are just variables, but they're given a value when you call a function
        Also known as formal parameters

        Arguments: Values that will be used by formal parameters, when we call a function
            Passed during function call.


        Python arguments are passed by assignment. The behaviour is similar to pass by reference,
        when passing a mutable object. For immutable objects, the behaviour is closer to pass by value.

        But note that neither of those terms really describe how arguments are passed, in Python.

        'Pass by reference' and 'pass by value' don't have any sensible meaning, in Python
        
        References:
        https://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_sharing
        https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference

        Positional Arguments: 
            Pos arguments are assigned to the parameters in the order they appear. In fact, the arguments in this 
            example(multiply()) are really called positional or keyword arguments.

        Functions that are not returning explicitly, returns 'None'.

'''


def multiply(x, y):
    """Returns the product of two numbers x and y

    Args:
        x (int): Number1
        y (int): Number2

    Returns:
        int: Returns the product of two numbers
    """
    res = x * y
    return res


def is_palindrome(string):
    """This function checks whether given string is a palindrome.

    Args:
        string (str): Take string as input

    Returns:
        bool: Returns True if string is a palindrome, False otherwise
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    """The functions check for the sentence whether it's a palindrome
    sentence without including the whitespaces and punctuation marks.

    Args:
        sentence (str): Takes a string as a sentence from the user

    Returns:
        boolean: Returns True if the sentence is a palindrome, False otherwise
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return is_palindrome(string)


ans = multiply(10.5, 4)
print(ans)

# word = input("Enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome.".format(word))
# else:
#     print("'{}' is not a palindrome.".format(word))

# sentence = input("Enter a sentence to check: ")
# if palindrome_sentence(sentence):
#     print("'{}' is a palindrome.".format(sentence))
# else:
#     print("'{}' is not a palindrome.".format(sentence))


