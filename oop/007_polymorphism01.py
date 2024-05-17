
########################################################################
#
# Duck typing demo
# If its walking like a duck, then its definately a duck
#
########################################################################

def drive(car):
    if hasattr(car, 'drive'):
        car.drive()
    else:
        print(f"`{car.name}` object has no attribute `drive`")


class Creta:

    def __init__(self, name="Creta") -> None:
        self.name = name

    def drive(self):
        print("Driving Creta")


class Mercedes:
    
    def __init__(self, name="Mercedes") -> None:
        self.name = name

    def drive(self):
        print("Driving Mercedes")


if __name__ == '__main__':
    c = Creta()
    c.drive()
    drive(c)
    c = Mercedes()
    drive(c)
