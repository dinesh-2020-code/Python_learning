from math import pi

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius
    

c1 = Circle(4)
print("Area of circle with radius " + str(c1.radius) + " is ", c1.area())
print("Perimeter of circle with radius " + str(c1.radius) + " is ", c1.perimeter())
