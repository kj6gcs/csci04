#Loops: while loops
#Loops allow you to repeat code as long as some condition (True/False) is True.
#while condition:
#    whatever is in your loop must be indented, it will repeat.

#Making an actual while loop
#Before we do anything, we're going to need variables.
#In any project, your variables should all be declared at the top of the program/top of current function.
x = 1 #interger variable called x with the number 3 (it is initialized)

#Now that I actually have a variable, I can start a loop using it.
#Our loops for now will based on comparisons: comparing some value to another.
#Loops can be INFINITE, which means they never end.
#   Usually this is because the condition is ALWAYS true.
#   Your loops need to end at some point.  They must have an eit condition.
#       (meaning, there is a situation where the condition they run on is false)
#       so your condition must be false at some point.
while x < 5:    #Is x less than 5?  If it is, this statement is true and we will loop.
    print("X is less than 5.")
    #Because this loop compares X to something, we won't get out of the loop
    #   unless X changes somehow.
    x = x + 1