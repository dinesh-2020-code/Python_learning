"""
    Subsets: A is a subset of B if  elements of A are member of B (A <= B)
    A proper subset is a subset that also isn't equal to the set that contains it. (A < B)
    Superset: A >= B
    Proper Superset : A > B
"""

animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat',
           }
birds = {'Robin', 'Swallow', 'Wren'}

print(f'Birds is a subset of animals: {birds.issubset(animals)}')   # birds <= animals
print(f'animals is a superset of birds: {animals.issuperset(birds)}')

print(f'Birds is a superset of animals: {birds.issuperset(animals)}')

print('*' * 80)

garden_birds = {'Swallow', 'Wren', 'Robin'}
print(garden_birds == birds)  # True
print(garden_birds <= birds)  # True
print(garden_birds < birds )  # check for proper subset returns False

print('*' * 80)

more_birds = {'Wren', 'Budgie', 'Swallow'}
print(garden_birds >= more_birds)  # False
