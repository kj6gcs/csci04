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
      
  //    1. Assign 20 to a variable named d. Divide d by 4 and assign the result to d, then print the result.
      int d = 20;
      d = d / 4;
      cout << d << endl;
  
   
  //    2. Create an integer variable called x, initialize it with 0. Then, create a while loop that will repeat as long as x equals 0. Inside the loop, add 1 to x and put the result back into x. Does this create an infinite loop?
  
      int x = 0;
      while(x == 0) {
          x = x + 1;
      } 
  
  
  
  //    3. Create a string variable and assign it the value "Yes". Create a do-while loop that will repeat as long as that variable equals "No". Within the loop, print the string variable. Does this create an infinite loop?
      string answer = "Yes";
      
      do {
          cout << answer;
      } while(answer == "No");
  
  
   
  
      return 0; //Your program will end after this line
  }