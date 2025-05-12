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
      // Start writing your code here!
      // Do-while loops are a special version of while loops
      // Like any loop, a do-while loop repeats some block of code as long as some condition is true
      // do-while loops follow similar syntax to while loops, however, do-while loops do not START with a condition--the condition is at the end
      // Key difference: do-while loops will ALWAYS run at least one time, while loops might not run at all

      // to make a do-while:
      // do { code in loop } while(condition);
      int y = 5; // if you're going to use a variable in a condition, the variable must exist AND have a value before you use it.
      do {
        cout << "In the loop...\n";
      }         while (y != 5); // condition goes at te bottom--even if it's false, this loop will run one time

      // What if we did a while loop instead?
      // while loops are useful when you need to repeat something, but you don't know exactly how many times you need to repeat
      // while loops , there's also a possibility that your loop will not run at all, if that's OK, while loops are good.
      while(y != 5) {
        cout << "in while loop!\n";
      }
  
      return 0; //Your program will end after this line
  }
  
   