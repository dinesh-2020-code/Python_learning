# string formatting

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))   # {ind:field-width}

print()

# align values to the left
# > right aligned values
# < left aligned values
# ^ center aligned values (caret symbol)
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))   # {ind:field-width}

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:<62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))


name = 'Mahadev'
age = 10000
print()
# f-strings
print(name + f" is {age} years old.")
print(f"Pi is approximately {22 / 7:12.50f}")
