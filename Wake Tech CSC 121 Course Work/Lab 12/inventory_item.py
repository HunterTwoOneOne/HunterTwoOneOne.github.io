#
# Instructor Provided File
# 8/5/2024
# Inheritance and Polymorphism - Problem 1 & 2
#
# Students: DO NOT CHANGE THIS FILE. Use it as the base class
# for your Book, Game, and DVD classes

class InventoryItem:
    def __init__(self, item_name, item_count, unit_cost, item_category):
        """
        This method is the class constructor. It sets the attributes of
        the class object with what is passed in by the calling routine.

        :param item_name: Name of the inventory item
        :param item_count: Number of item in inventory
        :param unit_cost: Unit cost of item
        :param item_category: Category of item
        """
        self.name = item_name
        self.count = item_count
        self.cost = unit_cost
        self.category = item_category

    # For get_item_input(), we will not be asking the user to
    # enter a category. That category will be filled in by the
    # subclasses that use this base class.
    def get_item_input(self):
        """
        This method will ask the user for item data and store it
        in the class object's attributes.

        :return:
        """
        # Get item name
        item_name = input('Enter the item name: ')
        # Get item count
        while True:
            try:
                item_count = int(input('Enter the item count: '))
                if item_count < 0:
                    print('Item count must be 0 or greater.')
                else:
                    break
            except:
                print('Item count must be an integer.')
        # Get unit cost
        while True:
            try:
                unit_cost = float(input('Enter the unit cost: '))
                if unit_cost < 0:
                    print('Unit cost must be 0 or greater.')
                else:
                    break
            except:
                print('Unit cost must be an floating point number.')

        self.name = item_name
        self.count = item_count
        self.cost = unit_cost

    def __str__(self):
        """
        This method will return a human-readable version of the
        class object.

        :return: Human-readable string representing the object.
        """

        return f'{self.name}\n' +\
               f'\tCount: {self.count}, Cost: {self.cost:.2f}\n' +\
               f'\tCategory: {self.category}'
