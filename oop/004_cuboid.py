class Cuboid:

    def __init__(self, length, breadth, depth):
        self.length = length
        self.breadth = breadth
        self.depth = depth
    
    def __init__(self):
        print("0 arg ctor")

    def lid_area(self):
        return self.length * self.breadth
    
    def total_area(self):
        return (2 * (self.length * self.breadth + self.breadth * self.depth + self.length * self.depth))
    

c1 = Cuboid()
# c2 = Cuboid(10, 4, 2)
# c3 = Cuboid(10)
