available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

'''
    'in' with a dict: 
        When you use 'in' with a list, it checks the items in a list. When you use 'in' with a dict, it checks the keys
        in the dict - not the values.
    print("mouse" in available_parts) # False
    print("4" in available_parts)     # True
'''

current_choice = None
computer_parts = {}   # create an empty dict
while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # if it's already in, so remove it
            print(f"Removing '{chosen_part}'")
            del computer_parts[current_choice]
        else:
            print(f"Adding '{chosen_part}'")
            computer_parts[current_choice] = chosen_part
        print(f"Your dict now contains: {computer_parts}")
    else:
        print("Please add options from the list below:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")

print(f"Your shopping list now contains: {computer_parts}")
