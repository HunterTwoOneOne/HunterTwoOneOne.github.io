# Nathanael Long
# 09/26/2025
# Problem 1 - Nested Lists

def main():

    """
    This is a function that gets the assignment scores for Ashley, Barb, and Carl,
    stores them in lists, and then does some adjustments to the scores.

    Steps:
    1. Prompts the user to enter assignment scores:
       ~ Ashley's scores: 3 scores
       ~ Barb's scores: 5 scores
       ~ Carl's scores: 4 scores
    2. Stores the provided scores in a nested list.
    3. Applies 5% extra credit to each score.
    4. Calculates the score spread for each student.
    5. Prints the modified scores and the original input scores.

    """

    # Get the Scores for Ashley, Barb, and Carl.
    # Based on the Sample, I'm giving Ashley 3, Barb 5, and Carl 4 Scores to be entered.
    print("Please enter Ashley's scores.")
    a_list = [int(input("Enter assignment score: ")) for _ in range(3)]
    print("Ashley's scores :", a_list)

    print("\n Please enter Barb's scores.")
    b_list = [int(input("Enter assignment score: ")) for _ in range(5)]
    print("Barb's scores :", b_list)

    print("\n Please enter Carl's scores.")
    c_list = [int(input("Enter assignment score: ")) for _ in range(4)]
    print("Carl's scores:", c_list)

    # Create a nested list for all the scores
    all_scores = [a_list[:], b_list[:], c_list[:]]
    print("\n All scores :", all_scores)

    # Add the 5% extra credit
    for score in range(len(all_scores)):
        for score_2 in range(len(all_scores[score])):
            all_scores[score][score_2] = int(all_scores[score][score_2] * 1.05)
    print("All scores after factoring in extra credit :", all_scores)

    # Create score spreads
    score_spread = []
    for scores in all_scores:
        score_spread.append(max(scores) - min(scores))
    print("Score spread :", score_spread)

    # Print the original scores
    print("\nOriginal Assignment Scores")
    print("Ashley's scores :", a_list)
    print("Barb's scores :", b_list)
    print("Carl's scores :", c_list)

main()