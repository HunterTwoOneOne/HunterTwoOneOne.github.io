#
# Nathanael Long
# 08/21/2025
# Calculating Sales Tax and final totals for sales.
#
# Test Case:
# Books - 7
# DVDs - 4
# Games - 6
# Cost before Tax - $ 63.15
# Sales Tax - $ 4.10
# Cost after Tax - $ 67.25
#


# Sales Tax is set to 6.5%
# Take Inputs for items

books = int(input("How many Books? "))
dvds = int(input("How many DVDs? "))
games = int(input("How many Games? "))

# Assign prices to each item
# Books are $2.25 each
# DVDs are $4.35 each
# Games are $5.00 each

books_total = (books * 2.25)
dvds_total = (dvds * 4.35)
games_total = (games * 5.00)

# Begin taking calculations for tax and final sale price and provide the output to the user

total_cart = books_total + dvds_total + games_total
print(f"Cost before Tax ${total_cart : .2f} ")
tax = total_cart * 0.065
print(f"Sales Tax ${tax : .2f} ")
final_total = total_cart + tax
print(f"Cost after Tax ${final_total : .2f} ")