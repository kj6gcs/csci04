// Starting C++ Now! //
// C++ basic skeleton code //

/* These first two lines are required for the code to work
Similar to importing libraries/modules in Python, like we did with the "random" module */
#include <iostream>
using namespace std;
  
  // First, comments.  In Python, comments use the # symbol, but in C++ they use // 
  // This is a comment (on one line) //
  /* This makes a comment lock.
    All lines beneath this one will become comments--until you close the block.
    All
    comments
    every line*/

//This is a function.  Specifically, the main() function.  In C++, all programs will start running
//from the main.  Whatever the first line of code in this function is, is the first line
//that will actually run.
int main() { //Code that comes after this bracket, and before it's closing bracket, is inside of this function
            //and will run when the function does.
      //Start writing your code here!
      //The first line of your program that will actually run is this.

      //We need variables.  How do you make a variable in C++?
      //Like in Python, in C++, variables must have a name, and they mjust be initialized (put something in them)
      //There is a difference: when you make a variable in C++, you MUST include what data type it is first.
      //In C++, there is STRONG TYPING.  Once a variable is declared with a certain type, it will stay that type forever.
      //For this project... what variables do we need?
      //We need 2 variables to hold inputs from the user, and one to hold the results of our math.
      float num1 = 0; //Float type variable (number w/decimal point), called num1, initialized to 0.
      //In C++, almost every line of code MUST END WITH A ; (semicolon) 
      float num2 = 0;
      float result = 0;

      //Now that we have bariables, we have places to store data--such as user input
      //We need to get numers from the user into our num1 and num2.
      //In C++, input/output use cin (input) and cout (output)
      //To properly take input in any language, you should tell the user what to do
      cout << "Enter the first number: "; //This prints some words
      //To take input, that itself is another step:
      cin >> num1;  //This will get input from the user into num1.
      //equivalent to python: num1 = float(input("Enter the first number: "))

      //Second number
      cout << "Enter the second number: ";
      cin >> num2;

      //Now that we have something in our variables, let's print them
      cout << "You entered: " << num1 << " and " << num2 << endl;
      
      //Time for math!
      //Addition
      result = num1 + num2; //Add together num1 and num2, put result into variable
      cout << "Addition: " << result << endl;
      //Subtraction
      result = num1 - num2;
      cout << "Subtraction: " << result << endl;
      //Multiplication
      result = num1 * num2;
      cout << "Multiplication: " << result << endl;
      //Division
      result = num1 / num2;
      cout << "Division: " << result << endl;

      return 0; //Your program will end after this line
  }