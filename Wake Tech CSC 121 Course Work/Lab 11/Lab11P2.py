# Nathanael Long
# 11/13/2025
# Classes and OO Programming - Problem 2

# I like a Dill Pickle personally. Whole. Not quartered or in slices.
import pickle
from inventory_item import InventoryItem, CATEGORY_LIST

def main():
    inventory_list = load_inventory()
    display_inventory(inventory_list)

    answer = ''
    while answer.lower() != 'n':
        item = InventoryItem()
        item.get_item_input()
        inventory_list.append(item)

        answer = input('Do you want to enter more items? (y/n): ')

    for category in CATEGORY_LIST:
        display_category(category, inventory_list)

    display_inventory(inventory_list)
    save_inventory(inventory_list)

def load_inventory():
    """
    Loads saved inventory data from inventory.dat and
    returns a list of from the data in the file.
    """
    try:
        with open("inventory.dat", "rb") as file:
            inventory_list = pickle.load(file)
            print("\nPrevious inventory loaded from inventory.dat.\n")
            return inventory_list
    except FileNotFoundError:
        return []

def save_inventory(inventory_list):
    """
    Saves the inventory list to inventory.dat.
    """
    with open("inventory.dat", "wb") as file:
        pickle.dump(inventory_list, file)
    print('\nInventory was saved in inventory.dat.\n')

def display_category(category_name, inventory_list):
    """
    Shows the inventory items in a category.
    """
    print()
    header = f'Items in {category_name}'
    divider = len(header) * '-'
    print(header)
    print(divider)

    found = False
    for item in inventory_list:
        if item.category == category_name:
            print(item)
            found = True

    if not found:
        print("No items.")

def display_inventory(inventory_list):
    """
    Shows the inventory that is currently stored or
    says that the inventory is empty.
    """
    print()
    print('The Current Inventory:')
    print('-----------------')

    if inventory_list:
        for item in inventory_list:
            print(item)
    else:
        print("The Inventory is empty.")

    print('-----------------')
    print()

if __name__ == "__main__":
    main()