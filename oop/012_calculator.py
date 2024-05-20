class Calculator:

    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return Exception("Cannot divide by zero!!!")


x = 10
y = 0

print(Calculator.add(x, y))
print(Calculator.subtract(x, y))
print(Calculator.multiply(x, y))
print(Calculator.divide(x, y))
