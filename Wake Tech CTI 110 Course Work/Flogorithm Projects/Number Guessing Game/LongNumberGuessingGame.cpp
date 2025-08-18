#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cmath>
#include <ctime>

using namespace std;

// Headers
string toString (double);
int toInt (string);
double toDouble (string);

int main() {
    srand(time(0));   //Seed random number generator
    

    // Long, Nathanael CTI-110-4136
    // A Number Guessing Game.
    // 
    // Test Cases:
    // 
    // Guessing -999 at any point will return the value - Sorry to see you quit, but thank you for playing! and the game will end, but the player will not be prompted to quit with this method until 1 wrong guess has been given.
    // 
    // Guessing wrong will return the following - Sorry, that wasn't right! and told to reguess.
    // 
    // If the guess is correct at any point, the player will be told - That's correct! Thank you for playing!
    // 
    // Test a wrong guess by providing any answer of 11 or higher as the game is not set to select a random number over 10.
    // 
    // Test quitting by giving -999 as the answer right away.
    // 
    // Test a correct answer by opening the Variable Watch Window and inputting the right answer.
    int randomRandint;
    int playerGuessedint;

    randomRandint = rand() % 10;
    cout << "Would you like to play a game?" << endl;
    cout << "Please guess a number between 0 and 10!" << endl;
    cin >> playerGuessedint;
    while (playerGuessedint != -999 && playerGuessedint != randomRandint) {
        if (playerGuessedint > 10) {
            cout << "Please only guess between 0 and 10!" << endl;
        } else {
            cout << "Sorry, that wasn't right! ";
        }
        if (playerGuessedint > randomRandint) {
            cout << "You guessed to high!" << endl;
        } else {
            if (playerGuessedint < randomRandint) {
                cout << "You guessed to low!" << endl;
            }
        }
        cout << "If you would like to quit, please enter the guess of -999." << endl;
        cout << "If you would like to keep playing, ";
        cout << "please guess a number between 0 an 10!" << endl;
        cin >> playerGuessedint;
    }
    if (playerGuessedint == -999) {
        cout << "Sorry to see you quit, but thank you for playing!" << endl;
    } else {
        cout << "That's correct! Thank you for playing!" << endl;
    }
    return 0;
}

// The following implements type conversion functions.
string toString (double value) { //int also
    stringstream temp;
    temp << value;
    return temp.str();
}

int toInt (string text) {
    return atoi(text.c_str());
}

double toDouble (string text) {
    return atof(text.c_str());
}
