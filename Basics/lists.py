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

empty_list = []
numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted("432985617")
print(digits) # prints the sorted list of each digit (stored as 'string' for ex: ['1', '2', '3', '4'...])

# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()

print(more_numbers)
print(numbers is more_numbers) # False
