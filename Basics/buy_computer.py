'''
    Buy computer program
    enumerate(): returns each item, with its index position.
'''
available_parts = ["Computer",
                    "Monitor",
                    "Keyboard",
                    "Mouse",
                    "Mouse Mat",
                    "HDMI Cable"]
current_choice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append(available_parts[int(current_choice) - 1])
        elif current_choice == '2':
            computer_parts.append(available_parts[int(current_choice) - 1])
        elif current_choice == '3':
            computer_parts.append(available_parts[int(current_choice) - 1])
        elif current_choice == '4':
            computer_parts.append(available_parts[int(current_choice) - 1])
        elif current_choice == '5':
            computer_parts.append(available_parts[int(current_choice) - 1])
        elif current_choice == '6':
            computer_parts.append(available_parts[int(current_choice) - 1])

    else:
        print("Please Add options from the list below")
        for number, item in enumerate(available_parts):  # enumerate returns pair (index, item)
            print("{}. {}".format(number + 1, item))

    current_choice = input()

print("You bought {}".format(computer_parts))


# more on enumerate()
for index, char in enumerate("abcdefgh"):
    print(index, char)

