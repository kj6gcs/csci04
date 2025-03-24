#Exercises
#Due at the end of class. No late submissions.
#Fill in the blanks with Python code to accomplish the following tasks. Number each piece of code to show what exercise it’s for. 
# When you’re done, show me the code so I can give you your points. (You do not need to turn it in through Canvas.)
#A quick reminder: to convert a value to another type (eg. string to integer), put parentheses around it with the new type outside 
# the parentheses. Remember that input() will always give you a string, even if you type a number (eg. typing 54 would actually get 
# you "54").

#Example: number = int(num) #convert the variable num into an integer, assign to the variable number

 

#1. Create a variable, initialize it to 0. Then, make a while loop that will count up by adding to that value, 
# #continuing as long as the counter is less than or equal to 10. Print the variable's value each time the loop repeats.
count = 0 #set initial value of variable
while count < 10:
    count += 1
    print("Count is: ", count)
print("final count is: ", count)
 

 

#2. Count up from 1 to 10 using a for-loop. Print the current number each time the loop repeats.
num = 0 #set initial value of variable
for num in range(1, 11, 1):
    print("The count is: ", num)

print("final count is: ", num)
 

 

#3. Count down from 20 to 1 using a for-loop. Print the current number each time the loop repeats.
x = 20 #set initial value of variable.  starts at 20 to be at the top of the count since we're deincrememnting here.
for x in range (20, 0, -1): #for loop start, sets "x" as variable, range set to count down by 1 each iteration from 20 to 0 (ends at 1)
    print("The countdown is: ", x)
print("You have reached: ", x)