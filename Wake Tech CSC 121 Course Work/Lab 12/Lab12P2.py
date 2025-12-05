#
# Nathanael Long
# 11/30/2025
# Inheritance and Polymorphism - Problem 2
#

import pickle
from inventory_item.py import InventoryItem
# No matter what I've tried I can't get it to load InventoryItem. I don't know what is wrong here.
from book.py import Book
from game.py import Game
from dvd.py import DVD

def main():
    # Calling load_inventory() should return a list of inventory items if
    # inventory.dat is present. If that file is not present, it should
    # return an empty list.
    inventory_list = load_inventory()
    display_inventory(inventory_list)

    answer_outer = ''
    while answer_outer.lower() != 'n':
        answer_inner = ''
        while answer_inner not in ['1', '2', '3']:
            answer_inner = input('What item type (1-Book, 2-Game, 3-DVD)? ')
            if answer_inner not in ['1', '2', '3']:
                print('Enter 1, 2, or 3.')

        # TODO - Create an appropriate object, ask the user for item input
        #  using the object's method, then append the object to the inventory
        #  list.

        if answer_inner == '1':
            obj = Book()
        elif answer_inner == '2':
            obj = Game()
        else:
            obj = DVD()

        obj.get_item_input()
        inventory_list.append(obj)

        answer_outer = input('Do you want to enter more items? ')

    display_inventory(inventory_list)
    save_inventory(inventory_list)


def load_inventory():
    """
    This function reads in a single list data structure from a
    binary file named inventory.dat and stores it in a variable
    that holds this inventory list data. The variable is returned.
    If the file does not exist, an empty list is returned.

    :return: List of all inventory objects
    """

    inventory_list = []
    # TODO - Attempt to load inventory data from a binary file named
    #  inventory.dat. If the file exists, load it into the inventory list.
    #  If the file does not exist, leave the inventory list empty.

    try:
        with open("inventory.dat", "rb") as f:
            inventory_list = pickle.load(f)
    except FileNotFoundError:
        pass
    return inventory_list

def save_inventory(inventory_list):
    """
    This function takes the inventory list and saves it to a binary
    file named inventory.dat.

    :param inventory_list: List of all inventory objects
    :return:
    """

    # TODO - Open a binary file named inventory.dat and dump the inventory
    #  list that has been passed in as a parameter to that file.

def save_inventory(inventory_list):
    with open("inventory.dat", "wb") as f:
        pickle.dump(inventory_list, f)
    print("Inventory.dat file was created.")

def display_inventory(inventory_list):
    """
    This function displays all the inventory items in the inventory.
    Each item's attributes are shown on a single line.

    :param inventory_list: List of all inventory objects
    :return:
    """

    print()
    print('Current Inventory')
    print('-----------------')
    # TODO - Display the inventory items that are in the inventory list
    #  that was passed in as a parameter. If the list is empty, display
    #  "Inventory is empty."
    if len(inventory_list) == 0:
        print("Inventory is empty.")
    else:
        for item in inventory_list:
            print(item)
    print('-----------------')
    print()


main()
