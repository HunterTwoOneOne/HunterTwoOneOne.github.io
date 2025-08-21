#
# Nathanael Long
# 08/21/2025
# This program calculates the time it takes to travel
# a certain distance going a specific speed.
#
# Note: The miles and speed entered could be a floating point
# number.
#
# Test Cases:
# 100 Miles at 20 MPH will take 5 Hours.
# 10 Miles at 1 MPH will take 10 Hours.
# 50 Miles at 25 MPH will take 2 Hours.


# Get the number of miles.
miles = float(input("Please do not enter non-number characters. Let's calculate travel times! Please enter your Milage... "))

# Get the speed in MPH.
speed = float(input('Please do not enter non-number characters. What will be your speed in MPH? '))

# Calculate the travel time.
travel_time = miles / speed

# Display the travel time (formatted to 2 decimal places).
print(f"You will travel this distance in {travel_time:.2f} hours!")