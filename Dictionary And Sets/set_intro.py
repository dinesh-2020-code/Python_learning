"""
    Introduction to sets
        -> A set is an unordered collection of objects with no duplicate entries. 
        -> The keys of a dictionary are very similar to a set. The main difference, since Python 3.7, is that
            dictionary keys are ordered.
        -> Sets have no ordering. There's no way to access individual items of a set.
        -> Checking for set membership : Can be checked with the help of `in` operator.
        -> Sets use hashes to store the items, anything that you want to put into a set must be hashable. If you try to
            put an object that is not hashable into a set, it will raise a `TypeError.
        -> If 'A' and 'B' are two sets, then
            1. Set union: Both elements of a set taken exactly once. Representation: A.union(B) or A | B
            2. Set intersection: Elements that are present in both sets. Representation: A.intersection(B) or A & B
            3. Set difference: Elements that are not present in both sets. Representation: A.difference(B) or A - B
            4. Set symmetric difference: Elements that are in one set or the other, but not both (Opposite of intersection)
                Representation: A.symmetric_difference(B) or A ^ B
            5. Subsets and supersets: We use normal coparison operators: <, <=, > and >= to check for subsets.

"""
farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

# checking for equality
more_animals = {'sheep', 'goat', 'hen', 'cow', 'horse'}
if farm_animals == more_animals:
    print("The sets are equal")
else:
    print("The sets are not equal")