#
# Nathanael Long
# 09/21/2025
# List Creation and Editing

# Needed for the random numbers we need later
import random

# Start of the actual list building and random number generation
# Low and Top refer to our lowest value and the top of the bounds
def generate_random_list(size, low, top):
    return [random.randint(low, top) for _ in range(size)]

def main():
    # Rewritten to be a comment since parameters aren't needed I guess. Thanks Josh.
    # We need the size of the list, the lowest value allowed, the highest value allowed, and to spit out
    # a set of numbers within those limits.

    # Ask for the number of items in the list as well as the minimum and maximum for the range of numbers
    size = int(input("How many numbers will be in these lists?  "))
    low = int(input("Please enter the minimum for the range of the random numbers:  "))
    top = int(input("Please enter the maximum for the range of the random numbers:  "))

    # Create the first random list
    list_1 = generate_random_list(size, low, top)
    print(f"List #1... :: {list_1}")
    list_2 = generate_random_list(size, low, top)
    print(f"List #2... :: {list_2}")

    print("Here is the list in pairs:  ")
    for number in range(size):
        print(f"Pair #{number+1}: {list_1[number]}, {list_2[number]}")

    # Join the two lists into one and print it
    # Something something we need to save Dr. Vance something something pick up that can.
    combine = list_1 + list_2
    print(f"The combined list: {combine}")

    # Sort the new list and print first three and last three
    combine.sort()
    print(f"The sorted list: {combine}")
    print(f" Here's the first three: {combine[0:3]}")
    print(f" Here's the final three: {combine[-3:]}")

    # Print the sum, the minimum, and the maximum
    num_sum = sum(combine)
    minimum = min(combine)
    maximum = max(combine)
    print(f"Total: {num_sum}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

    # Get the random numbers and check if they are in the list
    print("Random numbers for a check and potential removing:")
    for item in range(5):
        randomnumber = random.randint(low, top)
        if randomnumber in combine:
            index = combine.index(randomnumber)
            print(f"{randomnumber} found at -> Item #{index}")
            combine.pop(index)
        else:
            print(f"{randomnumber} was not found in the list.")

    # Print the new list
    print(f"List is created... :: {combine}")

main()