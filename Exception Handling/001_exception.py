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
    

try:
    pass
    
except (IndexError, ValueError):  # handling multiple exceptions in single `except` block
    pass
    

"""

# Index Error

lst = [10, 20, 30, 40]
try:
    index = int(input("Enter index: "))
    print(lst[index])
    print("End of try block")  # this statement will not be executed if exception is raised in line 21
except IndexError as e:
    print("Invalid index\n " , e)
    print(type(e))   # <class 'IndexError'>
except ValueError as e:
    print("Invalid type of index\n " , e)
except:
    print("Some other exception")

print("Terminated Gracefully...")