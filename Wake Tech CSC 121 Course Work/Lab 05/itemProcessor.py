#
# Nathanael Long
# 09/21/2025
# Module to help process item data
#

# Global Constants - Use these in your program where it makes sense
TAX_RATE = 0.065  # 6.5% sales tax
VOLUME_DISCOUNT = 0.95  # 95% of total is 5% off

def get_item_count(item_name, max_allowed, discount_threshold):
    """
    This function will ask the user to enter the number of items and
    validate the number entered is between 0 and the max_allowed
    inclusive. The number of items the user enters is returned.

    :param item_name: Name of item being prompted about
    :param max_allowed: Maximum number of items the user can enter
    :param discount_threshold: Minimum number of items eligible for 5% discount
    :return: Number of items entered by user (validated)
    """

    while True:
        try:
            items = int(input(f'Please give the number of {item_name} (maximum of {max_allowed}). '
                              f'({discount_threshold} or greater in order to receive a discount) :  '))
            if 0 <= items <= max_allowed:
                return items
            else:
                print(f"Please give a value 0 and {max_allowed}.")
        except ValueError:
            print("Please enter a valid number.")


def get_item_total(num_items, unit_price, discount_threshold):
    """
    This function calculates the total cost for the items and
    returns that value.

    :param num_items: Number of items
    :param unit_price: The cost of each item
    :param discount_threshold: Minimum number of items eligible for 5% discount
    :return: Total cost of item
    """

    total = num_items * unit_price
    if num_items >= discount_threshold:
        total *= VOLUME_DISCOUNT
    return total

def calc_and_display_receipt(book_total, dvd_total, game_total):
    """
    This function will calculate total before tax, the tax on the total,
    and the total after tax is added.

    The receipt should display the total cost of books, DVDs, and
    games IF the item cost is greater than 0. The receipt should also
    include the subtotal, tax, and total.

    :param book_total: Total cost of books
    :param dvd_total: Total cost of DVDs
    :param game_total: Total cost of games
    :return:
    """

    subtotal = book_total + dvd_total + game_total
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    if book_total > 0:
        print(f"Books: ${book_total:.2f}")
    if dvd_total > 0:
        print(f"DVDs: ${dvd_total:.2f}")
    if game_total > 0:
        print(f"Games: ${game_total:.2f}")
    print('_______________________________')
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
