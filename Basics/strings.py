# 'str' data type: string is a sequence of chars
#         01234567890123   indexed from 0..13
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])


# Negative indexing

print()
print(parrot[-1])
print(parrot[-14])

print()

print(parrot[3 - 14])  # parrot[-11]
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])
print()


# string slicing
print(parrot[0:6])  # Norweg index values from 0..5
print(parrot[-14:-8])
print(parrot[:9])   # Norwegian index values from 0..8
print(parrot[:-5])
print(parrot[10:14]) # Blue
print(parrot[10:])   # Blue
print(parrot[:6] + parrot[6:]) # Norwegian Blue
print(parrot[:]) # Norwegian Blue


# Slicing with negative numbers
#           01234567890123
#         -(43210987654321) 
# parrot = "Norwegian Blue"

print(parrot[-4:2])   # prints ""
print(parrot[-4:-2])  # prints "Bl"
print(parrot[-4:12])  # prints "Bl"


# using a step value in slice
print(parrot[0:6:2])    # prints "Nre"

number = "9,223;372:036 854,775;807"
separators = number[1::4] # ",;: ,;"
print((separators))

values = []
for char in number:
    if char not in separators:
        values.append(char)
    else:
        values.append(" ")

print(values)

values = "".join (v for v in values)
print(values)

print(values.split())
print([int(val) for val in values.split()])