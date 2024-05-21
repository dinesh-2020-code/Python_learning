# else block will be executed when there is no exception raised in try block. 
# In case of exception raised in try block, except block will be executed only not else block.

# Finally block will be executed regardless of exception raised or not. (Exceuted always)
# finally block will be exexuted if there is `return` statement encountered before it. Python will first
# execute the statements inside `finally` block, then return the value if applicable. The behavior is
# same if exception is raised (first `finally ` block then python will raise exceptions)
# Why finally block?
#     -> used for cleanup (releasing resources  like closing files, closing database connections etc.)

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
finally:
    print("Finally block")

print("Outside try-except-else block")
