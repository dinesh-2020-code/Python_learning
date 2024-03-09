'''
    Buy computer program
    enumerate(): returns each item, with its index position.
'''
available_parts = ["Computer",
                    "Monitor",
                    "Keyboard",
                    "Mouse",
                    "Mouse Mat",
                    "HDMI Cable",
                    "DVD drive"
                    ]
current_choice = "-"
computer_parts = [] # create an empty list
# add valid choices of items
valid_choices = [str(i) for i in range (1, len(available_parts) + 1)]  # list comprehension
while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int (current_choice) - 1
        chosen_item = available_parts[index]
        computer_parts.append(chosen_item)

    else:
        print("Please Add options from the list below")
        for number, item in enumerate(available_parts):  # enumerate returns pair (index, item)
            print("{}. {}".format(number + 1, item))

    current_choice = input()

print("You bought {}".format(computer_parts))


# more on enumerate()
# for index, char in enumerate("abcdefgh"):
#     print(index, char)


# list comprehensions
# l = [i for i in range(1, 5)] # [1, 2, 3, 4]

# print(valid_choices)
