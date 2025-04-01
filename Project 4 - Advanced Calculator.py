 #*************************************************************************
 # Your Name:           Robby Wideman
 # Project Due Date:    04-02-2025
 # Project Name:        Project 4: Advanced Calculator
 # CSCI-4:              Intro to Programming
 # Spring 2025
 # Project Description: Calculator Script That Requires Users to Input
 # Numbers & an Operator, and Loops Until User Enters "q"
 #*************************************************************************

#Write your code under this line*******************************************


def operatorValidation(num1, operator, num2):
    if operator == '+': #addition operator
        result = num1 + num2
        return f"{num1} + {num2} = {result:.2f}\n"  #this return does addition on the variables
    elif operator == '-': #subtraction operator
        result = num1 - num2
        return f"{num1} - {num2} = {result:.2f}\n"
    elif operator == '*': #multiplication operator
        result = num1 * num2
        return f"{num1} * {num2} = {result:.2f}\n" #this one does multiplication
    elif operator == '/': #division operator
        if num2 == 0: #just in case someone tries to get sneaky
            return "Are you trying to implode the universe?  You can't divide by zero!\n" #easter egg message for trying to divide by zero!
        result = num1 / num2
        return f"{num1} / {num2} = {result:.2f}\n" #actual division math
    elif operator == '^':  #exponentiation operator (aka a # to the power of another #)
        result = num1 ** num2  #the easier of the python operators to calculate expotents is "**"
        return f"{num1} ^ {num2} = {result:.2f}\n" 
    else:
        return "You can only enter the following operators: +, -, *, /, ^(for exponentiation)" #this is the message the user receives if they 
                                                                                                #enter anything other than a designated operator

#before getting too deep, we need a function to perform calculations based upon user "operator" input:
#this function will request the required input from the user, as well as check for the quit command, breaking the loop and exiting the 
#program if the user enters a Q or q
def calculations():
    while True:
        num1 = input("Enter the first number or 'q' to quit: ") #here we will take in num1 as a string to enable us to also take in the q for quit command.
        if num1.lower() == 'q':                                 #we will later convert it to a float
            print("Exiting Program")
            break

        operator = input("Enter the mathematical operator: ") #here we will take in the operator after the first number.  I find this a little less confusing
        if operator.lower() == 'q':                             #as this is probably the order of entering things in a calculator most people are used to.
            print("Exiting Program")
            break

        num2 = input("Enter the second number or 'q' to quit: ") #here we will take in num1 as a string to enable us to also take in the q for quit command.
        if num2.lower() == 'q':
            print("Exiting Program")
            break

        try:
            num1 = float(num1) #this converts the number entered as a string input above into a float number.  this was so it could accept Q/q to return 
                                #an error message to the user.
            num2 = float(num2)
            math = operatorValidation(num1, operator, num2) #this takes the inputs and checks them against the operatorValidation function to ensure 
                                                            #everything is entered as required
            print(math) #this takes all the validation function operations, math results, etc., and prints them so the user sees them as a completed 
                        #equation for what they entered
        except ValueError:
            print("Please ensure you've entered a valid number or operator.") #aka telling the user they entered something incorrectly

#variable definitions are handled in the functions above

#and our main section of code really isn't all that much, as all the heavy lifting is handled above in the functions =)

#everyone loves a welcome message:
print("\n>>>Project 4: Advanced Calculator<<<\n")
print(">>>You will enter your first number, second number, and then the operator to use on the two numbers<<<\n")
print(">>>Enter 'q' at any point to quit the program<<<\n")
print(">>>Only +, -, *, /, and ^ (for exponentiation) are valid operators<<<\n")

#this will actually perform all the calculations gathered from above:
calculations()
