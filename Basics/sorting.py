
# sorted() can be used to sort any iterable object
# pangram = "The quick brown fox jumps over the lazy dog"
# letters = sorted(pangram) # Return a new list containing all items from the iterable in ascending order.
# print(letters)

# numbers = [2.3, 4.5, 3.1, 1.6]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)

# another_sorted_numbers = numbers.sort() # Sort in-place and change the original list 'numbers'
# print(numbers)
# print(another_sorted_numbers) # prints 'None' to the console and sort() method doesn't return anything

# Case in-sensitive sorting
missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)

print(missing_letter)


names = ["Graham",
         "John",
         "terry",
         "eric", 
         "Terry", 
         "michael"
        ]

names.sort(key=str.casefold)
print(names)
