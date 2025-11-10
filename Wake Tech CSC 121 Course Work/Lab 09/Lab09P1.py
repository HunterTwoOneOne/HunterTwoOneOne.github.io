# Nathanael Long
# 10/30/2025
# Word counting in dictionaries
#

# DO NOT UPDATE ANY PART OF THE MAIN FUNCTION
def main():
    input_file = open('words.txt', 'r')  # Open a file for reading
    file_text = input_file.read().upper()  # Read all contents and convert to uppercase
    process_file(file_text)
    input_file.close()


def process_file(text):
    """
    This function creates a dictionary of words and their counts from the input text.
    It then identifies the words that appear the most in the dictionary, displays
    those words (with their count), and then removes them from the dictionary.
    Finally, it extracts and sorts the remaining words as a list and displays it.

    :param text: Text string to be parsed into a dictionary
    :return:
    """

    # Create Dictionary called wordstxt_dict
    wordstxt_dict = {}

    # Split data from words.txt apart
    wordstxt = text.split()

    # Count words and add them to the dictionary
    for words in wordstxt:
        if words in wordstxt_dict:
            wordstxt_dict[words] += 1
        else:
            wordstxt_dict[words] = 1

    # Print the dictionary
    print('Here is the contents of the dictionary:')
    print(wordstxt_dict)

    # Create and print the words with a list with the maximum count
    maxwordscount = max(wordstxt_dict.values())
    maxcountwords = [words for words, count in wordstxt_dict.items() if count == maxwordscount]
    print()
    print(f'Here are the words at the maximum of {maxwordscount}: {maxcountwords}')

    # Remove the words with max count from and then print dictionary
    for words in maxcountwords:
        del wordstxt_dict[words]
    print()
    print('Here is the contents of the updated dictionary:')
    print(wordstxt_dict)

    # Add the words in the dictionary in a list, sort, and print the sorted list.
    sortedwordstxt = sorted(wordstxt_dict.keys())
    print()
    print('Here are the contents sorted:')
    print(sortedwordstxt)

main()