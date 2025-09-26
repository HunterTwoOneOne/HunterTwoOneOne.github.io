# Nathanael Long
# 09/26/2025
# Problem 3 - List Comprehensions

def main():

    """
    This is a function that works with the application of list comprehensions
    using two predefined lists and various assignment required operations.

        Steps:
        1. Defines two starting lists: list_1 and list_2.
        2. Creates list_3: numbers 0–5 transformed with the expression (number * 2 - 3).
        3. Creates list_4: nested pairs [Step_C, Step_C_2] generated from ranges,
           filtered so that Step_C is odd and Step_C_2 is even.
        4. Creates list_5: the cube of each number in list_1.
        5. Creates list_6: each element of list_1 multiplied by 3.
        6. Creates list_7: a combined product/sum of elements from list_1 and list_2.
        7. Creates list_8: string combinations of elements from list_1 and list_2 joined with the "@" symbol.
        8. Prints each resulting list after its creation.

    """

    # Step A - Establish the Predefined lists
    list_1 = [4, 5, 8, 2]
    list_2 = [2, 5, 9]

    # Step B - List comprehension
    list_3 = [number * 2 - 3 for number in range(6)]
    print("Step B:", list_3)

    # Step C - More list comprehension
    list_4 = [[Step_C, Step_C_2] for Step_C in range(4) for Step_C_2 in range(5) if Step_C % 2 == 1 and Step_C_2 % 2 == 0]
    print("Step C:", list_4)

    # Step D - Even more list comprehension
    list_5 = [Step_D ** 3 for Step_D in list_1]
    print("Step D:", list_5)

    # Step E - Take a guess what the rest of the comment will be... it's more list comprehension
    list6 = [Step_E * 3 for Step_E in list_1]
    print("Step E:", list6)

    # Step F - You're not ready for this... it's more list comprehension
    list_7 = [Step_F * Step_F_2 + Step_F for Step_F in list_1 for Step_F_2 in list_2]
    print("Step F:", list_7)

    # Step G - Back at it again with more list comprehension
    list_8 = [f"{Step_G}@{Step_G_2}" for Step_G in list_1 for Step_G_2 in list_2]
    print("Step G:", list_8)

main()