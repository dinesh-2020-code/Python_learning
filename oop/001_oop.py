class Kettle(object):

    def __init__(self, make, price) -> None:
        self.make = make
        self.price = price
        self.on = False
    
    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

print(kenwood.on)
Kettle.switch_on(kenwood)  # the instance has to be passed when calling the method using class name, the instance would be passed onto 'self'
print(kenwood.on)
# data attributes: variables when bound to the class instance

print ("*" * 80)

kenwood.power = 1.5
print(kenwood.power)

# print(hamilton.power)  # AttributeError: 'Kettle' object has no attribute 'power'
"""
Class: template for creating objects. All objects created using the same class will have the same characteristics
Object: an instance of a class.
Instantiate: Create n instance of a class
Method: a function defined in a class.
Attribute: a variable bound to an instance of class
self: it's the reference to the instance of the class
constructor: a special method that is executed when an instance of a class is created. __init__() here. 
"""