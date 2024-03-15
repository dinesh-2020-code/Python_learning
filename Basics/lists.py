'''
    Lists in Python: Enclosed in Square brackets
    Diff b/w strings and lists: Strings are immutable while lists are mutable

    Immutable: An object that can't be changed
        ex: int, float, bool, str, tuple, frozenset, bytes
        like int '5' can't be changed, 5 is only 5, you can add int '1' to it, we wil get int '6' which is new int



'''


# computer_parts = ["computer",
#                   "monitor",
#                   "keyboard",
#                   "mouse",
#                   "mouse mat"
#                   ]

# for part in computer_parts:
#     print(part)

even = [0, 2, 4, 6, 8]
odd  = [1, 3, 5, 7, 9]

# print(min(even), end= ' ')
# print(max(even))

'''
    Methods and functions.

    A method is the same as a function, except that it's bound to an object
    That means we need an object, in order to call a method.
        for ex; s.append(x) # append() is a method which stating that it is called on sequence object.
            len(lst), min(lst) are functions
'''


# another_even = even
# print(another_even)
# even.extend(odd)
# print(even)
# even.sort(reverse=True) # even list sorted in descending order in-place i.e., not creating copying of original list
# print(even)
# print(another_even)

# empty_list = []
# numbers = even + odd
# print(numbers)

# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)

# digits = sorted("432985617")
# print(digits) # prints the sorted list of each digit (stored as 'string' for ex: ['1', '2', '3', '4'...])

# # more_numbers = list(numbers)
# # more_numbers = numbers[:]
# more_numbers = numbers.copy()

# print(more_numbers)
# print(numbers is more_numbers) # False


computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
# print(computer_parts)

# # s[i:j] = t => slice of s from i to j is replaced by the contents of the iterable t
# print(computer_parts[3:])
# computer_parts[3:] = ["trackball"]
# print(computer_parts)

data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 191, 350, 360]

min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

del data[:stop]
print(data)
# process the high values in the list
start = 0
for i in range (len(data) - 1, -1, -1):   # traverse backwards
    if data[i] <= max_valid:
        start = i+1
        break

del data[start:]

print(data)



# Iterating backwards in the list.

data = [104, 101, 4, 105, 308, 103, 5,
         107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

# for index in range(len(data)-1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid: 
#         print(index, data)
#         del data[index]
#         # print(index)

# print(data)

# #reversed() in python

# top_index = len(data) - 1;  # index of last element in the 'data'
# for index, value in enumerate(reversed(data)):
#     if value < min_valid or value > max_valid:
#         print(top_index - index, value, data)
#         del data[top_index - index]


# print(data)


# Nested List

menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs", "bacon", "spam"],
    ["eggs", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "eggs", "spam", "spam", "bacon", "spam"],
    ]

# Challenge: Print all meals with the 'spam' removed.

# for meal in menu:
#     # print(meal)
#     item_list = []
#     for item in meal:
#         if item != "spam":
#             item_list.append(item)
#             print(item, end=', ')
#     print()
#     # print(item_list)

# Approach 2: By removing 'spam' from the meal_menu and then printing the meal. 

# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
    
#     print(", ".join(meal))
'''
    Function Sign: Tells how the Function is defined
                Includes the Function's name and the parameteres that it defines


    for ex: print() have following sign below
    
        print(*objects, sep=' ', end='\n', file=None, flush=False)
        args: sep, end, file and flush are keyword arguments (named arguments)
        if no value for 'file' will be used, file=sys.stdout would be used to write on stdout 
'''

# More on print()

# name = "Tim"
# age = 10

# print(name, age, "Python", 2024)
# print(name, age, "Python", 2024, sep=", ")
# print()

# for meal in menu:
#     items = ", ".join(item for item in meal if item != "spam")
#     print(items)
