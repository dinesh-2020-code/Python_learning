# numbers = {} # dict

# To create an empty set, you can use tuple unpacking as below
# numbers = {*""}  # <class 'set'>
numbers = set() # <class 'set'>
# Adding elements to set
# numbers.add(1)
# while (len(numbers) < 4):
#     next_value = int(input("please enter you next value: "))
#     numbers.add(next_value)
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from the list, to remove duplicates.
# unique_data = set(data)
unique_data = sorted(set(data))  # produces a list of the data in ascending order
print(unique_data)

# Create a list of unique colours, keeping the order they appear
# dict.fromkeys() method: This method create a new dictionary with keys from iterable and values set to value.
unique_data = list(dict.fromkeys(data))  # insertion order is preserved here.
print(unique_data)
