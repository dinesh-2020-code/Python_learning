
lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}
# The keys 'lion', 'elephant' and 'teddy' are references to the lists
# When we perform a shallow copy, the references are copied into the new dictionary
# things = animals.copy()  # shallow copy (3 lists are here not 6)
things = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list
}
print(things["teddy"])
print(animals["teddy"])

print()

# things["teddy"].append("toy")
teddy_list.append("toy")
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via `things`")
print(things["teddy"])   # ['cuddly', 'stuffed', 'toy']
print(animals["teddy"])  # ['cuddly', 'stuffed', 'toy']c


'''
    To create a deep copy of an object, Python has a 'copy' module that you can use.
    The 'copy' module provides a 'deepcopy()' function.
    Performing a deep copy will create copies of lists, dictionaries and other mutable objects, that are
    contained in whatever you're copying.
'''
