#
# Nathanael Long
# 11/30/2025
# Inheritance and Polymorphism - Problem 1 & 2 - dvd.py
#

"""
Used the same was as book.py &
contains the class used for dvd
information in the Lab.
"""

from inventory_item import InventoryItem

class DVD(InventoryItem):
    def __init__(self, item_name='', item_count=0, unit_cost=0.00, upc='', genre=''):
        super().__init__(item_name, item_count, unit_cost, "DVD")
        self.upc = upc
        self.genre = genre

    def get_item_input(self):
        super().get_item_input()

        while True:
            code = input("What is the UPC for this game? ")
            if len(code) == 12 and code.isdigit():
                self.upc = code
                break
            print("The UPC needs to be a 12 digit number please. ")

        # Genre input
        self.genre = input("What genre is this DVD? ")

    def __str__(self):
        return (super().__str__() +
                f"\n\tUPC: {self.upc}\n\tGenre: {self.genre}")
