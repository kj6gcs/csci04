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

  // To make an if statement,
  // if (condition) { code for if in brackets }
  // If's are NOT loops, do not repeat (unless you put them inside a loop..)
  int x = 0;
  //Take input
  cout << "Please type the number 5. ";
  cin >> x;
  cout << "X is: " << x << endl;
  if (x == 5) {
    cout << "X is equal to 5!\n";
  }


  return 0; //Your program will end after this line
}

