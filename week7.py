#If-then: makes a decision based on a condition
#    If your condition is True, run the code attacehd to the if
#    If your condition is False, do not run the code for the if
#Unlike loops, if-statements do not repeat by themselves

#If example
#if condition:
#    #the code for the if (will run if the condition is true)

#Else-ifs let you check more than one condition and do different things
# for different conditions
#if condition:
#    Thing for first condition
#elif condition:
#    Thing for second condition

#Let's make an if-statement that checks if a number is 5 or not
num = int(input("Type a number! "))     #put the number 5 into the num variable

#Make an if-statement, print something if the number is 5
if num == 5:
    print("The number is equal to 5!")

if num != 5:
    print("Not 5.")