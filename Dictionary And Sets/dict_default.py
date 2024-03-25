from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"Chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"Beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

print()
print("`pantry` now contains,...")
# print(sorted(pantry)) # returns the list of keys sorted alphabetically
for key, value in sorted(pantry.items()):
    print(key, value)
'''
    The diff between dict.setdefault() method and dict.get() method is that setdefault() method also adds the key to the
    dict in addition to returning the default value while dict.get() method doesn't modify the dict (it doesn't add any
    key to the dictionary)

'''
