# Nathanael Long
# 10/30/2025
# Random numbers in sets

"""
This is a program that generates 8 random numbers between 1 and 16.
It makes them into a set and then generates another set the same way.
It creates a union of the two sets and tells you the similarities,
the differences, and the numbers that are less than 10.
"""

# Prepare to generate random numbers
import random

def main():

    # Generate the first set and print it
    set_1 = {random.randint(1, 16) for _ in range(8)}
    print('Here is Set 1')
    print(f'\t{set_1}')
    print()

    # Generate the second set and print it
    set_2 = {random.randint(1, 16) for _ in range(8)}
    print('Here is Set 2')
    print((set_2))
    print()

    # Make a union of the two sets
    set12union = set_1 | set_2
    print(f'Here is the union of Set 1 and Set 2: \n\t{set12union}')
    print()

    # Show the similarities between the two sets
    set12intersect = set_1 & set_2
    print(f'Here are the similarities between Set 1 and Set 2: \n\t{set12intersect}')
    print()

    # Show the differences between set 1 and set 2
    set12dif = set_1 - set_2
    print(f'Here are the difference between Set 1 and Set 2: \n\t{set12dif}')
    print()

    # Show the symmetric differences between set 1 and set 2
    set12symdiff = set_1 ^ set_2
    print(f'Here is the symmetric difference between Set 1 and Set 2: \n\t{set12symdiff}')
    print()

    # Show the numbers that are less than 10 from the union
    set12below10 = {num for num in set12union if num < 10}
    print(f'Here are the numbers that are less than 10 in the union of set1 and set2: \n\t{set12below10}')

main()
