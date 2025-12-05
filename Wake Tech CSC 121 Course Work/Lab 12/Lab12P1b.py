#
# Nathanael Long
# 11/30/2025
# Inheritance and Polymorphism - Problem 1 & 2 - Lab12P1b.py
#

"""
Asks the user for information and
to build out what item is being
created and ensuring it gets stored
in the right spot.
"""

from book import Book
from game import Game
from dvd import DVD

def main():
    items = []

    for _ in range(3):
        choice = ''
        while choice not in ['1', '2', '3']:
            choice = input("What kind of item is this? (1-Book, 2-Game, 3-DVD): ")
            if choice not in ['1', '2', '3']:
                print("Please enter only 1, 2, or 3.")

        if choice == '1':
            obj = Book()
        elif choice == '2':
            obj = Game()
        else:
            obj = DVD()

        obj.get_item_input()
        items.append(obj)

    for item in items:
        print(item)

main()