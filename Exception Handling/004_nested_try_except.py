# Exceptions can be handled by multiple `except` blocks for single try block
# Nesting of try_except is not readable.

try:
    a = int(input("Enter first number: "))
    try:
        b = int(input("Enter second number: "))
        try:
            c = a // b
            print(c)
        except ZeroDivisionError as e:
            print(e)
    except ValueError:
        print("Value Error from inner")

except ValueError:
    print("Value Error from outer")