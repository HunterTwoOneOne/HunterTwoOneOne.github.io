# Nathanael Long
# 09/26/2025
# Problem 2 - Tuples

import random

def main():

    """
    This is a function that uses tuple operations by generating random numbers
    within a stated range and manipulating them.

    Steps:
    1. Prompts the user for:
       - The number of values to generate (t)
       - The start and end of the random number range
    2. Creates a tuple of t random integers in the given range.
    3. Extracts:
       - The first 4 elements as a tuple
       - The last 2 elements as a tuple
    4. Concatenates these two tuples into one.
    5. Creates a new tuple with each element incremented by 1.
    6. Displays all intermediate and final results.

    """

    print("\n Step A : ")
    t = int(input("How many values will be added? "))

    print("\n Step B : ")
    start = int(input("What is the start of the range? "))
    final = int(input("What is the end of the range? "))

    print("\n Step C : ")
    numbers = tuple(random.randint(start, final) for _ in range(t))
    print("Tuple of ",t, "random numbers:", numbers)

    print("\n Step D : ")
    tuple_start = numbers[:4]
    print("Tuple of starting 4 numbers:", tuple_start)

    print("\n Step E : ")
    tuple_final = numbers[-2:]
    print("Tuple of final 2 numbers:", tuple_final)

    print("\n Step F : ")
    tuple_concatenated = tuple_final + tuple_start
    print("Two tuples concatenated:", tuple_concatenated)

    print("\n Step G : ")
    tuple_incremented = tuple(x + 1 for x in tuple_concatenated)
    print("Two tuples concatenated and incremented:", tuple_incremented)

main()