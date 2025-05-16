/*************************************************************************
 * Your Name:           Robby Wideman
 * Project Due Date:    May 21st, 2025 by 2359 Hours
 * Project Name:        Project 9 - Word Choice C++
 * CSCI-4:              Intro to Programming
 * Spring 2025
 * Project Description: A program that will take input strings of word from
 * the user and has the user choose one of the words to print.
 *************************************************************************/

/* These first two lines are required for the code to work
   Similar to importing libraries/modules in Python, like we did with the "random" module */

#include <iostream>
#include <string>          // This library is used to work with strings in C++.
#include <windows.h>       // This is required to use a sound clip.
#include <mmsystem.h>      // This is required to use a sound clip.
#pragma comment(lib, "winmm.lib")  // This is required to use a sound clip.

using namespace std;

// Colors and styles for the program!
#define RESET   "\033[0m"
#define RED     "\033[31m"
#define GREEN   "\033[32m"
#define YELLOW  "\033[33m"
#define BLUE    "\033[34m"
#define CYAN    "\033[36m"
#define BOLD    "\033[1m" 
#define ORANGE  "\033[38;5;208m"
#define SILVER  "\033[38;5;250m"
#define COBALT  "\033[38;5;20m"
#define MAGENTA "\033[35m"

/* I've been reading a lot about coders putting ASCII art in their code as Easter Eggs.
   This isn't an easter egg, but I'm a big fan of the movie Short Circuit, 
   and Johnny 5 is always asking for MORE INPUT! Instead of putting the art in the middle of my code 
   where it's going to run, I created a void function to "do its job and exit" after laying down 
   some Johnny 5 / Short Circuit art! */
void printJohnny5Art() {
    cout << ORANGE << "\nNeed input!" << RESET << endl;
    cout << "             " << SILVER << "_//)_//)" << endl;
    cout << "            / /)=/ /)" << endl;
    cout << "           (" << BLUE << "(" << CYAN << "O" << BLUE << ")" << SILVER << "=" << BLUE << "(" << CYAN << "O" << BLUE << ")" << SILVER << ")" << endl;
    cout << "              " << ORANGE << "\\" << COBALT << "||" << ORANGE << "/" << endl;
    cout << "      " << SILVER << "________" << COBALT << "====" << SILVER << "____" << RED << "[o]" << SILVER << "_" << endl;
    cout << "  )/)|___._==      ==_.___|(/(" << endl;
    cout << " (( \\ || '-.________.-' || / ))" << endl;
    cout << "  \\=/ ||     .." << COBALT << "''" << SILVER << "..     || \\=/" << endl;
    cout << "   \\\\_//    / " << RED << "[" << YELLOW << "||" << RED << "]" << SILVER << " \\    \\\\_//" << endl;
    cout << "    \\V/    / " << GREEN << "......" << SILVER << " \\    \\V/" << endl;
    cout << "           \\" << COBALT << "::::::::" << SILVER << "/" << endl;
    cout << "     _____." << SILVER << "---" << COBALT << "'  '" << SILVER << "---._____" << endl;
    cout << "    |_-_-_|" << SILVER << "__" << COBALT << "------" << SILVER << "__|_-_-_|" << endl;
    cout << "    |_-_-_|" << COBALT << "=        =" << SILVER << "|_-_-_|" << endl;
    cout << "    |_-_-_|          |_-_-_|" << endl;
    cout << "    |_-_-_|          |_-_-_|" << RESET << endl;
}

// This function enables ANSI colors in the pop out terminal.
void enableAnsiColors() {
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD dwMode = 0;
    GetConsoleMode(hOut, &dwMode);
    dwMode |= ENABLE_VIRTUAL_TERMINAL_PROCESSING;
    SetConsoleMode(hOut, dwMode);
}

int main() {
    enableAnsiColors(); // Enable fancy ANSI colors in supported terminals

    // Setting up an array to hold a 5 word string
    string words[5];        // Array to reference the string entered by the user and give the words indices.
    string userInput;       // Variable to hold the user's string input.
    char repeatChoice;      // Variable to hold the user's choice of word to print.
    char proceed;           // Declaring a variable to use for the user's choice to proceed or exit.

    // Welcome Message:
    cout << BOLD << BLUE << "Welcome to the Word Choice Program!" << endl;
    cout << "You'll next enter a short string 5 words." << endl;
    cout << "Then you'll choose one of the words to print." << RESET << endl;

    // Starting menu, users can choose to proceed or exit.
    cout << GREEN << "Would you like to proceed? (y/n): " << RESET << endl;
    cin >> proceed;

    if (proceed == 'n' || proceed == 'N') {
        cout << BOLD << RED << "Well, fine then, Laser Lips!  I didn't want to see your sentence anyway!  GOOD DAY!" << RESET << endl;
        PlaySound(TEXT("goodDay.wav"), NULL, SND_FILENAME | SND_SYNC);
        return 0;
    }

    // Take in user's string input:
    do {
        printJohnny5Art(); // Here's Johnny!

        cout << ORANGE << "\nPlease enter a string of 5 words. Punctuation is not included in word count." << RESET << endl;
        for (int i = 0; i < 5; i++) {
            cin >> words[i];
        }
        cout << endl << endl;

        // Display the words entered by the user:
        cout << BLUE << "You entered the following string / words / sentence: " << RESET << endl;
        for (int i = 0; i < 5; i++) {
            cout << words[i] << " ";
        }
        cout << endl << endl;

        // Ask the user to choose a word to print:
        int wordChoice = 0;
        while (true) {
            cout << ORANGE << "Please choose a word to print (1-5): " << RESET << endl;
            cin >> wordChoice;

            if (wordChoice >= 1 && wordChoice <= 5) {
                cout << BLUE << "\nYou chose: " << words[wordChoice - 1] << RESET << endl << endl;
                break;
            } else {
                cout << RED << "\nWOW!  You were literally told to pick a number between 1 and 5 and you chose " << wordChoice << " instead!  Try again!" << RESET << endl;
                cin.clear();
                cin.ignore();
            }
        }

        cout << GREEN << "Would you like to go again? (y/n): " << RESET << endl;
        cin >> repeatChoice;

    } while (repeatChoice == 'y' || repeatChoice == 'Y');

    cout << RED << "\nWell, fine then, Laser Lips!  I didn't want to see your sentence anyway!  GOOD DAY!" << RESET << endl;
    PlaySound(TEXT("goodDay.wav"), NULL, SND_FILENAME | SND_SYNC);

    system("pause");
    return 0;
}