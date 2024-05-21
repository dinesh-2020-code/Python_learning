
def div(a, b):
    if b != 0:
        c = a // b
        return c
    else:
        raise ZeroDivisionError("Division by zero:- not possible!!!")
    

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    c = div(a, b)
    print("Try block executed successfully")
except ZeroDivisionError as err:
    print("in exception block:\n" , err)
else:
    print(f"{a} // {b} is {c}")

print("Outside try-except-else block")