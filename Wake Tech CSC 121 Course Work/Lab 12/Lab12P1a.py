#
# Nathanael Long
# 11/30/2025
# Inheritance and Polymorphism - Problem 1 & 2 - Lab12P1a.py
#

"""
Contains the information from
dvd/book/game.py to be used/modified
as needed.
"""

from book import Book
from game import Game
from dvd import DVD

def main():
    items = [
        Book("Python Now", 100, 22.95, "2345234523451"),
        Book("Even More Python", 150, 8.95, "3456345634561"),
        Game("Uno", 75, 6.95, "123456789012"),
        DVD("Barbie", 50, 12.00, "098765432121", "Comedy"),
        DVD("The Piano", 10, 2.90, "321321321321", "Drama")
    ]

    for item in items:
        print(item)

main()