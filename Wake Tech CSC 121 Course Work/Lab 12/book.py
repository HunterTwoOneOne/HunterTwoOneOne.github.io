#
# Nathanael Long
# 11/30/2025
# Inheritance and Polymorphism - Problem 1 & 2
#
from inventory_item import InventoryItem

class Book(InventoryItem):
    def __init__(self, item_name='', item_count=0, unit_cost=0.00, isbn13=''):
        """
        This method is the class constructor. It sets the attributes of
        the class object with what is passed in by the calling routine.

        :param item_name: Name of item
        :param item_count: Number of item in inventory
        :param unit_cost: Unit cost of item
        :param isbn13: ISBN of the book
        """
        super().__init__(item_name, item_count, unit_cost, "Book")
        self.isbn13 = isbn13

    def get_item_input(self):
        """
        This method will ask the user for item data and store it
        in the class object's attributes.

        :return:
        """

        super().get_item_input()

        while True:
            isbn = input("What is the ISBN for this book? ")
            if len(isbn) == 13 and isbn.isdigit():
                self.isbn13 = isbn
                break
            print("The ISBN needs to be a 13 digit number please. ")

    def __str__(self):
        """
        This method will return a human-readable version of the
        class object.

        :return: Human-readable string representing the object.
        """

        return (super().__str__() + '\n' +
                f'\tISBN: {self.isbn13}')
