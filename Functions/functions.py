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

'''


def multiply(x, y):
    res = x * y
    return res


ans = multiply(10.5, 4)
print(ans)