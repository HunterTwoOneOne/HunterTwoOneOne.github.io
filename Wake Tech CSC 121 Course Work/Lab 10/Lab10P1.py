# Nathanael Long
# 11/09/2025
# Use dictionary comprehensions

def main():

    text = input('Enter a string: ').upper()

    # This code counts the number of vowels in the user input
    # and outputs a dictionary of the results.

    vowels = 'AEIOU'
    letter_count = {v: text.count(v) for v in vowels if v in text}
    print(f'Vowel Count: {letter_count}')

    # This code determines the vowels that appear the least number
    # of times in the user input and outputs a dictionary of the
    # results.

    min_count = min(letter_count.values())
    min_letter_count = {k: v for k, v in letter_count.items() if v == min_count}
    print(f'Letter Min: {min_letter_count}')

main()
