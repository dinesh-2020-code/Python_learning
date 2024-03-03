
a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0

print()

# In python, you can't use float where 'int' is required (strongly typed behaviour of python)
for i in range(1, a // b):
    print(i)

