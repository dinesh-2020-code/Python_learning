"""
    Dictionaries and Sets:
        NOT sequences: can't access items using index positions
        When dealing with items in a dictionary, we use a `key` to get individual values from the dictionary
        Dictionary stores key-value pairs (also referred to Mapping)
        Python `dict` is equivalent to a Java `HashMap`

        A set is an unordered collection of things. There's no way to retrieve a specific item from set.


    Dictionay:
        A dictionary is a collection of 'values', that are stored using a 'key'.
        for ex: dict of employees in a company stored as {empId, empName}
        Each value in a dictionary has a unique key that's used to refer to it.
"""

vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple'
}

# accessing value from dict - If 'key' doesn't exist in dict, then it will give KeyError
# my_car = vehicles['fiesta']
# print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get('er5')
# print(learner)

# If 'key' doesn't exist, get() method will return 'None', whereas indexing will crash with a KeyError
# get() method is useful when you aren't sure whether 'key' exists or not
# indexing is faster than get() method.


# Iterating over dictionary
# for key in vehicles:
#     print("{}: {}".format(key, vehicles[key]))

# Adding values to the dict
vehicles["starfighter"] = "Rafale"
vehicles['toy'] = 'Glider'

# Changing values in a dict
vehicles['virago'] = 'Yamaha XV305'

# Removing items from dict
del vehicles["starfighter"]
# del vehicles["f1"]          # KeyError: 'f1' as this key doesn't exists in dict
# vehicles.pop("f1")   # KeyError: 'f1'
result = vehicles.pop("f1", None)
print(result) #prints 'None'


dreamCar = vehicles.pop('dream')
print(dreamCar)   # prints 'Honda 250T'

# dict.pop() method returns the value corresponding to the key, if key exists 
# otherwise returns the default value passed as second arg to .pop() method.
# If second argument not passed and key doesn't exists in dict, then it will throw
# 'KeyError'

# del dict['key'] is faster than dict.pop() in terms of performance
for key, value in vehicles.items():
    print(key, value, sep=": ")

'''
    .items() in Python 2
        You might come across that inefficient loop if you find yourself modifying or converting old Python2 code
        .items() in Python2 created a list. That means it needed a copy of the data, and used more memory.
        For that reason, programs might have used the simple for loop, to avoid the extra memory overhead of using 
        .items()
        
        Python2.2 added a .iteritems() method, which works in a similar way to Python3's .items() method.
        Python3 now uses something called a generator, and doesn't copy the data from the dictionary.
        With Python3, remember to use 'enumerate()' when iterating over sequences, and .items() when iterating
        over dicts.
        
        .items() method returns an iterator of tuples, and we unpack the tuples into our `key` and value `variables`
        
    Changes to Python Dictionaries
        If you installed Python from the python.org website, the implementation of Python that you installed from that 
        site is called CPython.
        
        That's because most of the implementation is written in 'C'.
        There are other implementations of Python: for example 'IronPython' (or IPython) and 'Jython'.
        
        'CPython' is the reference implementation of Python - the version written by Guido Van Rossum.
        Version 3.6 of 'CPython' changed the way that dictionaries worked.
        In earlier versions, the keys of a dictionary were unordered. That means you could get the keys printed in a 
        different order, each time you run the program.
        If you're using 'Python3.5', and the dictionary prints in a different order each time, now you know why that is.
        
        'Python3.6' preserved the insertion order of dictionary keys. That means you'll always iterate over them in the 
        same order.
        That was an implementation detail, which meant you couldn't rely on that behaviour in other implementations of
        Python 3.6.
        
        With 'Python 3.7', that behaviour became part of the language.
        When you iterate over a dictionary with 'Python 3.7 and above, the keys will appear in th order they were added
        to the dictionary.
        
        That's something you need to be aware of, because you can get a different order in earlier versions of Python. 
        'Python 3.5' goes out of support in Sept 2020- but that doesn't mean people will stop using it.
        But it does mean that it's acceptable for you to specify that your code requires 'Python 3.6' or higher, if you 
        rely on features introduced in that version.
'''

