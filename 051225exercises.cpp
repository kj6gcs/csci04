/*************************************************************************
 * Your Name:
 * Project Due Date:
 * Project Name:
 * CSCI-4: Intro to Programming
 * Spring 2025
 * Project Description:
  *************************************************************************/
  
/*These first two lines are required for the code to work
  Similar to importing libraries/modules in Python, like we did with the "random" module */

#include <iostream>
using namespace std;

 

int main() {
    //Start writing your code here!
    //Input and output--the prompting for input--are separate things in C++.
/* 1. The user should be prompted to enter a number, which should be put into a variable. If the number is equal to 0, print “Equal to zero.” 
If the number is greater than 0, print “Greater than 0.” If the number is less than 0, print “Less than 0.”*/
    int num = 0;

    cout << "Enter a number" << endl;
    cin >> num;

    if (num == 0) {
        cout << "Equal to zero" << endl;
    } else if (num > 0) {
        cout << "Greater than 0" << endl;
    } else {
        cout << "Less than 0" << endl;
    }
    

/* 2. The user should be prompted to enter two numbers, which should be put into two different variables. If the first number is greater 
than the second, print “First is greater.” If the second number is greater than the first, print “Second is greater.” Otherwise, if they are equal,
 print “The numbers are equal.” */

    int num1 = 0;
    int num2 = 0;

    cout << "Enter your first number" << endl;
    cin >> num1;
    cout << "Enter your second number" << endl;
    cin >> num2;

    if (num1 > num2) {
        cout << "First is greater." << endl;
    } else if (num1 < num2) {
        cout << "Second is greater." << endl;
    } else {
        cout << "The numbers are equal" << endl;
}
 

    return 0; //Your program will end after this line

}


 

 