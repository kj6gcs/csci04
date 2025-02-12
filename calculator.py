 #*************************************************************************
 # Your Name:           Robby Wideman
 # Project Due Date:    02-19-2025 by 2359 Hours
 # Project Name:        Project 1 - Calculator
 # CSCI-4: Intro to Programming
 # Spring 2025
 # Project Description: (description of what the code does)
 #*************************************************************************

#Write your code under this line*******************************************

#first make variables to hold our numbers.
#to take input in Python, you must use input()

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#print to show the numbers went in correctly

print("You entered:", num1,"and",num2)

#in order for your inputs to be numbers, YOU HAVE TO TELL THE COMPUTER TO MAKE THEM NUMBERS.
#need 3rd variable to hold math results.

result = num1 + num2

#after math, print the answer.

print("Addition:",result)

#variable name on left, value on right, every time.

#more math:

result = num1 - num2
print("Subtraction: ", result)


result = num1 * num2
print("Multiplication: ", result)

result = num1 / num2
print("Division: ", result)