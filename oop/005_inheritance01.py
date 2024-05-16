class Rectangle:
    """Rectangle class used to represent rectangel with length and breadth as its dimensions"""

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Cuboid(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)  # Calling the ctor of parent class explicitly
        # We can also initialize the properties of the parent class directly in the child class ctor.
        # self.length = length
        # self.breadth = breadth
        # self.height = height
        print(dir(self))

    def volume(self):
        return self.length * self.breadth * self.height


# r = Rectangle(10, 5)
# print(r.area())
# print(r.perimeter())

c = Cuboid(10, 5, 3)
print(c.volume())
