from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def show(self):
        pass

    def display(self):
        print("Parent display")


class Child(Parent):

    def show(self):
        return print("Child show")
    

c = Child()
c.show()
c.display()
