# Nathanael Long
# 11/13/2025
# Classes and OO Programming - Problem 1 (Lab11P1.py)

'''
    This program works with inventory_item.py and
    has the items: Python for All, Barbie, and Uno.
    It assigns the count, cost, and category for
    each item. It requests information for a
    new entry from the user.
'''

from inventory_item import InventoryItem

def main():
    # Create three preset items
    item1 = InventoryItem("Python for All", 10, 12.95, "Book")
    item2 = InventoryItem("Barbie", 15, 6.95, "DVD")
    item3 = InventoryItem("Uno", 32, 4.50, "Game")
    print(item1)
    print(item2)
    print(item3)

    new_item = InventoryItem()
    new_item.get_item_input()
    print(new_item)

if __name__ == "__main__":
    main()