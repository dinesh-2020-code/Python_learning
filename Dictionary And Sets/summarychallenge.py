choice = "-"
while choice != "0":
    if choice in set("12345"):
        print(f"You chose {choice}")
    else:
        print("Please choose your option form the list below:")
        print("1:\tLearn Pyhon")
        print("2:\tLearn Java")
        print("3:\tLearn Swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")
    
    choice = input()

"""
    -> Set is faster than when u use a list because set use hash codes - just like keys in a dict.
    -> A hash code lets us go directly to the item in the hash table.
    -> There's a small overhead while the hash code is calculated, but once that's done, access is very fast.
    -> If you're working with large data, checking for membership will be lot faster with a set, compared to a list.
"""