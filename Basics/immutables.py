# res = True
# another_res = res
'''
    id() method returns the identity of an object. This is an integer which is guaranteed to be unique
    and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have same id() 
    value.
'''
# print(id(res))
# print(id(another_res))
# res = False
# print(id(res))
# print(id(another_res))

res = "Correct"
another_res = res
print(id(res))   # 2338478117680
print(id(another_res))  # 2338478117680

res += " the code"
print(id(res))   # 2338479653680 id got changed this signifies that the strings are immutable
print(id(another_res)) # 2338478117680 

# what happened above is that the python can't change the strings as it is immutable. 
# what it does that it created new string and bind the name res to the new string.
