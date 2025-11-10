# Nathanael Long
# 11/09/2025
# Trish's Bookstore Inventory System
#
import pickle
import os

CATEGORY_LIST = ['Book', 'DVD', 'Game']

def main():
    inventory_counts, inventory_costs, inventory_categories = read_inventory_file()

    print("Welcome to Trish's Inventory Input System")
    print("Current Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_categories)

    response = ''
    while response != '0':
        display_menu()
        response = input('Enter your choice: ')

        if response == "1":  # Add an item
            item_name, item_count, unit_cost, category = get_item_input()
            inventory_counts[item_name] = item_count
            inventory_costs[item_name] = unit_cost
            inventory_categories[item_name] = category
            print(f"{item_name} added to inventory.")
        elif response == "2":  # Display a single item
            item_name = input('Enter item name: ')
            if item_name in inventory_counts:
                print(f"\n{item_name}")
                print(f"\tCount: {inventory_counts[item_name]}, Cost: {inventory_costs[item_name]:.2f}")
                print(f"\tCategory: {inventory_categories[item_name]}")
            else:
                print(f"{item_name}: Not found")
        elif response == "3":  # Display items in a category
            category_name = input('Enter category name: ')
            print(f'\nItems in {category_name}:')
            if category_name in CATEGORY_LIST:
                items = [item for item, cat in inventory_categories.items() if cat == category_name]
                if items:
                    for i in items:
                        print(f"\t{i}")
                else:
                    print(f"\tNo items found in {category_name}")
            else:
                print(f'{category_name} not in list of categories: {CATEGORY_LIST}')
        elif response == "4":  # Delete a single item
            item_name = input('Enter item name: ')
            if item_name in inventory_counts:
                del inventory_counts[item_name]
                del inventory_costs[item_name]
                del inventory_categories[item_name]
                print(f"{item_name} deleted.")
            else:
                print(f"{item_name}: Not found")
        elif response == "5":  # Display all inventory
            display_all_inventory(inventory_counts, inventory_costs, inventory_categories)
        elif response != "0":
            print("Invalid choice. Try again.\n")
        print()

    # Exit steps
    print("Final Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_categories)
    save_inventory_file(inventory_counts, inventory_costs, inventory_categories)


def display_menu():
    print("What would you like to do?")
    print("(1) Add an item\n"
          "(2) Display an item\n"
          "(3) Display a category\n"
          "(4) Delete an item\n"
          "(5) Display all inventory\n"
          "(0) Exit")


def display_all_inventory(inventory_counts, inventory_costs, inventory_categories):
    if not inventory_counts:
        print("== Empty ==")
        return

    # Left-aligned columns for readability
    print(f"{'Item name':<14}  {'Count':<7}  {'Unit Cost':<10}  {'Category':<20}")
    print(f"{'-'*14}  {'-'*7}  {'-'*10}  {'-'*20}")

    for item in inventory_counts:
        print(f"{item:<14}  {inventory_counts[item]:<7}  {inventory_costs[item]:<10.2f}  {inventory_categories[item]:<20}")


def save_inventory_file(inventory_counts, inventory_costs, inventory_categories):
    with open("inventory.dat", "wb") as f:
        pickle.dump(inventory_counts, f)
        pickle.dump(inventory_costs, f)
        pickle.dump(inventory_categories, f)
    print("Inventory saved to inventory.dat.")


def read_inventory_file():
    inventory_counts, inventory_costs, inventory_categories = {}, {}, {}
    if os.path.exists("inventory.dat"):
        with open("inventory.dat", "rb") as f:
            inventory_counts = pickle.load(f)
            inventory_costs = pickle.load(f)
            inventory_categories = pickle.load(f)
    return inventory_counts, inventory_costs, inventory_categories


def get_item_input():
    item_name = input('Enter the item name: ')
    while True:
        try:
            item_count = int(input('Enter the item count: '))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Item count must be an integer.')
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Unit cost must be a number.')
    while True:
        category = input('Enter the category: ')
        if category not in CATEGORY_LIST:
            print(f'Category must be in this list: {CATEGORY_LIST}')
        else:
            break
    return item_name, item_count, unit_cost, category


main()
