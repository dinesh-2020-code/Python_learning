from contents import pantry, recipes
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# print(display_dict)


def add_shopping_item(data: dict, item: str, quantity: int) -> None:
    """Adds a tuple containing `item` and `quantity` to the `data` dict."""
    # check if item is already there in shopping list
    # If item is there, it will append the more quantity needed
    # If item is NOT in shopping_list, it will create a new key and add.
    # data[item] = data.get(food_item, 0) + quantity
    # dict.setdefault() method will check for the key passed as argument in the dict,
    #           If key exists returns the value of the key
    #           If key doesn't exist, it will create a new key and assign a default value to it (0 here)
    data[item] = data.setdefault(item, 0) + quantity
    # if item in data:
    #     data[item] += quantity
    # else:
    #     data[item] = quantity


display_dict = {}
# print(list(enumerate(recipes)))  # returns the list of tuples (x, y) where x is the index from 0 and y is the 'key'
'''
    Enumerating over dictionary keys
        The enumerate() takes each of the keys from the dictionary, generates the next number for each one, and emits
        both value as a tuple.
'''
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

# print(display_dict)
shopping_list = {}

while True:
    # Display a menu of your recipes.
    print("Please choose a recipe from below given recipes:")
    print("-" * 50)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")
    if choice == "0":
        break
    elif choice in display_dict:
        selected_recipe = display_dict[choice]
        print(f"You have selected: '{selected_recipe}'")
        print("checking ingredients...")
        ingredients = recipes[selected_recipe]  # 'ingredients' is also a dict containing  pairs of (item, quantity)
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if quantity_in_pantry >= required_quantity:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}.")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for things, amount in shopping_list.items():
    print(f"Required {things}: {amount}")
