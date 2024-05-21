# Exeception Handling
# Exception: Run time errors (Traceback is returned for run time errors)
# Errors: Syntax, Logical, Run time errors(exceptions)
# Exception handling construct
"""
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
"""

# Index Error

lst = [10, 20, 30, 40]
try:
    index = int(input("Enter index: "))
    print(lst[index])
    print("End of try block")  # this statement will not be executed if exception is raised in line 21
except:
    print("Invalid index")

print("Terminated Gracefully...")