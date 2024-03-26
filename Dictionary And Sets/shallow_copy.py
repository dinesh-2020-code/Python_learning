import copy

from simple_deepcopy import dict_deep_copy

# animals = {
#     "lion": "scary",
#     "elephant": "big",
#     "teddy": "cuddly",
# }
# # things = animals  # `things` and `animals` both are pointing to the same object (dict)
# things = animals.copy() # shallow copy of 'animals'
# animals["teddy"] = "toy"
# print(things)
# print(animals)

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}
# Perform a shallow copy
# things = animals.copy()  # shallow copy (3 lists are here not 6)

# Perform a deep copy
things = copy.deepcopy(animals)
# things = dict_deep_copy(animals)
print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])   # ['cuddly', 'stuffed', 'toy']
print(animals["teddy"])  # ['cuddly', 'stuffed']
