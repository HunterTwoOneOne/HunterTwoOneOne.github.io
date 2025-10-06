# Nathanael Long
# 10/05/2025
# Count uppercase letters in a string
#
import os

# DO NOT CHANGE ANY CODE IN THE MAIN FUNCTION
def main():
    try:
        input_file = open('strings.txt', 'r')  # Open a file for reading
        for line in input_file:  # Use a for loop to read each line in the file
            manipulate_text(line)
            print()
    except FileNotFoundError:
        print('Did not find strings.txt in current directory:')
        print(os.getcwd())


def manipulate_text(line):
    """
    This function accepts a string, performs various manipulations on the
    string, and outputs the results. It demonstrates many different str
    methods, operators, and functions from Lesson 7 of CSC-121.

    :param line: A text string to be manipulated
    :return:
    """
    print(line)   # DELETE THIS LINE
    # Strip the leading and trailing whitespace, and output the string.
    stripped_line = line.strip()

    # Replace all occurrences of $NAME with your first name.
    stripped_line = stripped_line.replace("$NAME", "Nathanael")

    # Replace all occurrences of $EMAIL with your email address.
    stripped_line = stripped_line.replace("$EMAIL", "nhlong@my.waketech.edu")

    # Replace all occurrences of $CITY with the name of the city where you live.
    stripped_line = stripped_line.replace("$CITY", "Raleigh")

    # Print the updated line.
    print(stripped_line)

    # Print a message indicating the number of characters in the updated line.
    print(f"Number of characters: {len(stripped_line)}")

    # Count the number of occurrences of your first name and print a message
    # reporting the count.
    name_count = stripped_line.count("Nathanael")
    print(f"Number of occurrences of first name: {name_count}")

    # Use floor division to divide the number of characters by 2, then print
    # the first half and last half of the line.
    midpoint = len(stripped_line) // 2
    first_half = stripped_line[:midpoint]
    second_half = stripped_line[midpoint:]
    print(f"First half: {first_half}")
    print(f"Second half: {second_half}")

    # Print the line in uppercase.
    print(stripped_line.upper())

    # Print the line in lowercase.
    print(stripped_line.lower())

main()
