'''
    Mutable object is one whose value can be changed.
        ex: list, dict, set, bytearray

    https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types

    if you wish to clear the whole mutable sequence, you can write as 
        1. seq *= 0 or seq *= x , where x can be any neg index.
        2. seq.clear()
        3. del s[:]

'''

shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list

print(id(shopping_list))   # 2012990887296
print(id(another_list))    # 2012990887296

shopping_list += ["cookies"]
print(shopping_list)
print(another_list)
print(id(shopping_list))  # 2012990887296
print(id(another_list))   # 2012990887296

# shopping_list and another_list both bounds to same object.

a = b = c = d = e = f = another_list # binding 6 diff names to same shopping list
a.append("cream")
print(c)

'''
    Strings are immutable. When we tried to change a string, Python created a new object-
    a new string and re-attached the name to it. 

    Lists are mutable - they can be changed. WHen we appended a new item, Python was able to change the 
    contents of the list, without creating a new one.
'''