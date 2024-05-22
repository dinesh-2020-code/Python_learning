# creating our own exception class

class MyError(Exception):
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self) -> str:
        return "Creating My exception" + "\n" + self.msg


try:
    raise MyError("This is my error")
except MyError as e:
    print(e)
