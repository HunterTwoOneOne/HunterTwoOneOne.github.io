import random
random.seed()   #Prepare random number generator


# Long, Nathanael CTI-110-4136
# A Number Guessing Game.
# 
# Test Cases:
# 
# Guessing -999 at any point will return the value - Sorry to see you quit, but thank you for playing! and the game will end, but the player will not be prompted to quit with this method until 1 wrong guess has been given.
# 
# Guessing wrong will return the following - Sorry, that wasn't right! and told to reguess.
# 
# If the guess is correct at any point, the player will be told - That's correct! Thank you for playing!
# 
# Test a wrong guess by providing any answer of 11 or higher as the game is not set to select a random number over 10.
# 
# Test quitting by giving -999 as the answer right away.
# 
# Test a correct answer by opening the Variable Watch Window and inputting the right answer.
randomRandint = int(random.random() * 10)
print("Would you like to play a game?")
print("Please guess a number between 0 and 10!")
playerGuessedint = int(input())
while playerGuessedint != -999 and playerGuessedint != randomRandint:
    if playerGuessedint > 10:
        print("Please only guess between 0 and 10!")
    else:
        print("Sorry, that wasn't right! ", end='', flush=True)
    if playerGuessedint > randomRandint:
        print("You guessed to high!")
    else:
        if playerGuessedint < randomRandint:
            print("You guessed to low!")
    print("If you would like to quit, please enter the guess of -999.")
    print("If you would like to keep playing, ", end='', flush=True)
    print("please guess a number between 0 an 10!")
    playerGuessedint = int(input())
if playerGuessedint == -999:
    print("Sorry to see you quit, but thank you for playing!")
else:
    print("That's correct! Thank you for playing!")
