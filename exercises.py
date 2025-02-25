#1. Calculate the sum of 15 + 20 and put the answer into a viariable called addition.  Print the result:
addition = 15 + 20
print(addition)

#2. Subtract 10 from 30 and put the result into a variable called subtraction.  Print the result.
subtraction = 30 - 10
print(subtraction)

#3. Assign the string "ball python" to a variable named snake.  Print the snake variable.
snake = "ball python"
print(snake)

#4. Assign 15 to a variable named c.  Subtract 5 from c, assign the result to a variable, and print the result.
c = 15
solved = c - 5
print(solved)

#5. Write a program that, using a loop, repeatedly takes an input into a variable called command, then prints the input.  Keep looping
#as long as the input is not equal to "stop."
command = "" #create command, put emmpty string in it.
while command != "stop": #creating loop condition
    #taking input...
    command = input("Make this stop? ")
    #print the input
    print("You typed: ", command)

#this is not an infinite loop, as it has a condition which will end the loop if met ("stop")