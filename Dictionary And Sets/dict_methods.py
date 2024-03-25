d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# d.values() method: D.values() -> an object providing a view on D's values
v = d.values()
print(v)

d[10] = "ten"
print(v)

print("four" in v)  # True
print("eleven" in v) # False
'''
    Dictionary View objects: 
        The objects returned by 'dict.keys()', 'dict.values()' and 'dict.items()' are 'view' objects. They provide a 
        dynamic view on the dictionary's entries, which means that when the dictionary changes, the view reflects these
        changes.
'''
# d2 = {
#     7: "lucky seven",
#     10: "ten",
#     3: "this is new three"
# }
#
# dict.update() method: update method will not change the positioning of the keys i.e., insertion order being preserved.
# d.update(d2)
# for key, value in d.items():
#     print(f"{key}: {value}")
#
# print()
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)

# class methods: We use class name to call methods
# dict.fromkeys() method: Create a new dictionary with keys from iterable and values set to `value` passed as 2nd arg
# .
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)

# dict.keys() method: D.keys() -> a set-like object providing a view on D's key
# keys = d.keys()
# print(keys)
#
# for item in d.keys():
#     print(item)

