/*************************************************************************
 * Your Name:           Robby Wideman
 * Project Due Date:    May 7th, 2025 by 2359 Hours
 * Project Name:        Project 7: C++ Calculator
 * CSCI-4:              Intro to Programming
 * Spring 2025
 * Project Description: A simple calculator built using the C++ language.
 * It will take two float numbers from a user, and perform basic math
 * equations (addition, subtraction, division, multiplication) on the 
 * 2 inputs.  It will then print the two numbers entered by the user and
 * show each formula being performed on those numbers, and their solutions.
  *************************************************************************/
  
 /*These first two lines are required for the code to work
  Similar to importing libraries/modules in Python, like we did with the "random" module */

#include <iostream>
#include <thread> // <- Used for sleep_for
#include <chrono> // <- Used in the fake pause while the program "crunches the numbers" lol
using namespace std;

// Also, you now I love to colorize my text!
#define RESET   "\033[0m"
#define RED     "\033[31m"
#define GREEN   "\033[32m"
#define YELLOW  "\033[33m"
#define BLUE    "\033[34m"
#define MAGENTA "\033[35m"
#define CYAN    "\033[36m"
#define BOLD    "\033[1m"   

// Here's the workhorse of the program!
int main() {
    // Start writing your code here!

    // I wanted to make this give the users to run again or quit, so I'm including some extras:
    char choice = 'C'; // This sets the choice to 'C' for continue upon the program starting (or
                       // else it could quit as soon as it started)

    do {

        // Initializing our 2 inputs (num1 & num2) and our results variables to 0:
        float num1 = 0;
        float num2 = 0;
        float result = 0;

        // Welcome Message.
        // Ask if they want to go again also.
        // Also, hang on to your seats, we're getting fancy with an ASCII-style header!
        cout << BLUE << "+===========================================+" << endl;
        cout << "|      Welcome to Robby's C++ Calculator    |" << endl;
        cout << "+===========================================+" << endl;
        cout << "|   [C]  Crunch some numbers!               |" << endl;
        cout << "|   [Q]  Quit this awesome calculator       |" << endl;
        cout << "+-------------------------------------------+" << RESET << endl;
        cout << RED << "Enter your choice: " << RESET;
        cin >> choice;

        // This part here will allow the user to exit the program from the get-go, if they want.
        if (choice == 'Q' || choice == 'q') {
            break;
        }      

        // Take inputs from user & provide them with basic instructions.
        cout << "Enter your first number: "; // Instructions for the user.
        cin >> num1; // Takes first input from user.
        cout << "Enter your second number: "; // More instructions for the user.
        cin >> num2; // Takes second input from user.

        // Let's show the users what they gave us:
        cout << "You entered: " << num1 << " and " << num2 << endl;

        // Fake thinking delay
        cout << "\nCrunching the numbers...\n\n";
        std::this_thread::sleep_for(std::chrono::seconds(2)); /*I had ChatGPT help me on this portion.  
        I think people like to think the computer has to think, lol! */

        // Make the math magic happen!
        cout << "Here are your solved equations: " << endl;

        // Addition:
        result = num1 + num2;
        cout << "Addition: " << num1 << "+" << num2 << "=" << result << endl;
    
        // Subtraction:
        result = num1 - num2;
        cout << "Subtraction: " << num1 << "-" << num2 << "=" << result << endl;

        // Division:
        // I love my divide by zero easter eggs:
        if (num2 != 0) {
            cout << "Division: " << num1 << " / " << num2 << " = " << num1 / num2 << endl; // Normal division operations
        } else {
            cout << RED << "DANGER, Will Robinson!" << "\nDivision: Cannot divide by zero!  What are you trying to do, destory the universe?!?!?!\n" << RESET << endl; // If they try to divide by 0!
        }

        // Multiplication:
        result = num1 * num2;
        cout << "Multiplication: " << num1 << "*" << num2 << "=" << result << endl;
  
    } while (choice != 'Q' && choice != 'q');

    // Exiting the program, in style!
    cout << "\nThanks for using the calculator, Robby-style!  Goodbye!" << endl << endl;
    system("pause"); // Added this to pause the terminal from closing before you can actually read the results lol
    return 0; //Your program will end after this line
  }