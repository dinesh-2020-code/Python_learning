class Kettle(object):

    power_source = "electricity"  # class attribute

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

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
"""
Class: template for creating objects. All objects created using the same class will have the same characteristics
Object: an instance of a class.
Instantiate: Create n instance of a class
Method: a function defined in a class.
Attribute: a variable bound to an instance of class
self: it's the reference to the instance of the class
constructor: a special method that is executed when an instance of a class is created. __init__() here.
class attribute: shared by all instances 

Constructors are not overloaded in Python, Python will shadow the all other constructors except one created recently
To safer side, don't write more than one constructor.

Instance variables: An object of a class (also known as instance). We can create multiple instances of a class and
    each instance of a class has its own value of variables (i.e., variables are not shared among instances) and such
    variables are known as instance variables.

    -> Instance variables can be declared inside __init__ method or any instance method or outside class as well.
        class Test:
            
            def __init__(self):
                self.a = 10

            def instance_method(self):
                self.b = 10

        
        t = Test()
        dir(t) // {dir contains `a` as instance variable, 'fun'}
        t.instance_method() 
        dir(t) // {dir contains `a` and `b` as instance variables, 'fun'}
        t.c = 20
        dir(t) # {dir contains `a`, `b` and `c` as instance variables, 'fun'}

Instance methods: The methods of a class accessing instance variables. The first parameter to instance methods will 
    always be `self`.

    -> 'self' is not a keyword, it's just a variable for storing the reference to the calling object.


Class/Static Variables and Class Methods:

    -> Class variables are shared among all instances of a class. Only one copy of class/static variables exist
        in the memory. The variables belong to class
    -> The methods accessing only class variables are known as 'class methods'

    class Rectangle:

        count = 0  # Class variable
        def __init__(self, length, breadth):
            self.length = length
            self.breadth = breadth
            Rectangle.count += 1

        def getLength(self):
            return self.length

        def getBreadth(self):
            return self.breadth

        def setLength(self, len):
            self.length = len

        def setBreadth(self, bre):
            self.breadth = bre

        def perimeter(self):
            return 2 * (self.length + self.breadth)

        def area(self):
            return self.length * self.breadth

        @classmethod
        def count_Rect(cls):
            return cls.count  

        @staticmethod
        def is_square(len, bre):
            return len == bre
            
        
    r1 = Rectangle(10, 4)
    r2 = Rectangle(11, 3)

    r1.count_Rect()  # 2
    r2.count_Rect()  # 2
    Rectangle.count_Rect() # 2

    r1.is_square(10, 10)  # True
    Rectangle.is_square(10, 10) # True


Static Methods:
    -> Methods that do not access instance and class variables of a class are known as static methods
    -> Defined using decorator `@staticmethod'
    -> Used to establish a relation between class and method

Accessors and Mutators: 
    -> Also Getters and Setters methods
    -> Accessor methods are used to get the value of an instance variable.
    -> Mutator methods are used to set/modify the value of an instance variable.

Inheritance: 
    -> Inheritance is the process by which one class takes on the attributes and methods of another.
    -> The class being inherited is called the parent class, and the class that inherits is called the child class.
    -> The child class inherits all the attributes and methods of its parent class.
    -> A child class can also have its own attributes and methods that are not present in the parent class.
    -> The child class is also called derived class, and the class from which it inherits is called the base class.
    -> A class can be derived from more than one base class in Python, this is called multiple inheritance.
    -> The order in which the base classes are mentioned is the order in which they will be searched for
    -> Every class in Python (directly or indirectly) is inherited from an `Object` class.

    -> If we are creating the object of child class, then only child class' constructor will be called by default. We need
    to explicitly call the parent class constructor.
    -> When we are creating the object of child class, we have 2 options with us, either initalize the parent class' properties
    inside child class' constructor or call the parent class constructor explicitly.


Inner/Nested classes
    -> Class inside other class

Polymorphism: 
    -> `Poly` means `many` and `morph` means `forms`.
    -> Polymorphism is the ability of an object to take on many forms.
    -> One object different actions. Which object is passed, the method of that object will be called at runtime.

"""
