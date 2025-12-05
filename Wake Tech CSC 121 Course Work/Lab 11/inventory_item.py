# Nathanael Long
# 11/13/2025
# Classes and OO Programming - Problem 1 (inventory_item.py)

'''
    This works in conjunction with the Lab11P2.py and
    Lab11P1.py files. It creates the class that works
    to manage data about the Books, DVDs, and Games
    that need to be tracked and stored.
'''

CATEGORY_LIST = ["Book", "DVD", "Game"]

class InventoryItem:
    def __init__(self, name="", count=0, cost=0.0, category=""):
        self.name = name
        self.count = count
        self.cost = cost
        self.cat = category

    def get_item_input(self):
        self.name = input("Enter the item name: ")

        while True:
            try:
                self.count = int(input("Enter the item count: "))
                if self.count < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a whole, non-negative number.")

        while True:
            try:
                self.cost = float(input("Enter the unit cost: "))
                if self.cost < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a non-negative number.")

        while True:
            self.cat = input("Enter the category: ").capitalize()
            if self.cat in CATEGORY_LIST:
                break
            else:
                print(f"Invalid category. Choose from: {', '.join(CATEGORY_LIST)}")

    def __str__(self):
        return (f"{self.name}\n"
                f"\tCount: {self.count}, Cost: {self.cost:.2f}\n"
                f"\t{self.cat}")
