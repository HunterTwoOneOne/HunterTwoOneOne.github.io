#
# Nathanael Long
# 08/30/2025
# Trish at Bargain Swap Shop Loyalty Reward Program
#

# Get the value for the customer's items
purchase = float(input("Enter the total purchase amount: "))

# Check if customer is eligible for the Loyalty Rewards Program
rewards = input("Is this customer in the Loyalty Rewards Program? ( yes [y] / no [n] ): ")

# Sales Tax Calculations
tax = 0.065
salestax = purchase * tax
total = purchase + salestax


giftcard = 000
if rewards == "yes" or rewards == "y":
    if 50 <= purchase <= 100:
        giftcard = 15
    elif purchase > 100:
        giftcard = 25
#Customer is NOT in the program but spends over 100$
else:
    if purchase > 100:
        giftcard = 5

print(f"Sales Tax: ${salestax:.2f}")
print(f"Total After Tax: ${total:.2f}")

if giftcard > 000:
    print(f"Give the customer a ${giftcard} Gift Card.")
else:
    print("The customer is not eligible to get a Gift Card.")