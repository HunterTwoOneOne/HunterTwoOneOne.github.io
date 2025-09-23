##
# Nathanael Long
# Sept 12th 2025
# Dice roll program
#

# Prepare to generate a random number
import random

# Establish variables
Crit = "CRITICAL HIT!"
Sword = "Sword"
Shield = "Shield"
Spell = "Spell"
Potion = "Potion"

# Get input and loop when input is not within 5-15
while True:
    Rolls_Num = int(input("How many rolls? (5 - 15) ->  "))
    if Rolls_Num not in range(5 , 16):
        print("Please only give a Number between 5 and 15")
    else:
        break

# Check for the outputs and print them
for Roll in range(Rolls_Num):
    Roll_D20 = random.randint(1 , 20)
    5

    if Roll_D20 == 20:
        print(f"Roll #{Roll + 1}: {Roll_D20} -> {Crit}")
    else:
        Remains = Roll_D20 % 4
        if Remains == 0:
            print(f"Roll #{Roll + 1}: {Roll_D20} -> {Sword}")
        elif Remains == 1:
            print(f"Roll #{Roll + 1} {Roll_D20} -> {Shield}")
        elif Remains == 2:
            print(f"Roll #{Roll + 1}: {Roll_D20} -> {Spell}")
        elif Remains == 3:
            print(f"Roll #{Roll + 1}: {Roll_D20} -> {Potion}")

# Thank the user and end the program
print("Thank you for playing!")