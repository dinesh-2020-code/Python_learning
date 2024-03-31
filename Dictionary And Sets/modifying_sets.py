# numbers = {} # dict

# To create an empty set, you can use tuple unpacking as below
# numbers = {*""}  # <class 'set'>
numbers = set() # <class 'set'>
# Adding elements to set
# numbers.add(1)
while (len(numbers) < 4):
    next_value = int(input("please enter you next value: "))
    numbers.add(next_value)
print(numbers)
