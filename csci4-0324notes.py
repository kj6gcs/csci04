#For Loop
#Repeat a specific number of times, for each item, in a sequence
#for variable in range(start,end)

for number in range(5): #If you only put one number, you'll start at 0
    #for each number in the range of 0-5
    #Because we put 5 by itself in the parentheses, we'll count up from 0 to 5
    #We'll count by adding 1 to the number variable each time the loop repeats
    print("number is:",number)

#Range is the condition, in the sense that the last number in the range decides when the loop ends.
#Once your variable is past the last number of the range, the loop ends
#In this case, the loop stops once number = 5, meaning it only prints up until 4
print("Out of the loop")
print("Final number:",number)

#For loops don't have to start from 0, they can start and end with any numbers you want.
#If you actually want the range of 1 to 5....
for number in range(1,5): #This will start at 1, end at 5 (you must go over 1 number than the highest you want)
        print("second number:",number)
    
print("Out of the loop:",number)

#range(start, end, increment or decrement)
#by default if you don't give a start (just one #) the number will be the end
#   and the start will be 0.
#If you don't give an increment (3rd number), the increment will be 1 (you'll add 1 to your variable each time the loop repeats)

for number in range(1, 10, 2):
#starts at 1, adds 2 each iteration, ends at 9 (1 under 10, and jumps by 2 due to the 3rd/increment number).
    print("third number:", number)

print("final number:",number)

#If you want a loop that counts DOWN, change the start and end, change the decrement
for negative in range(15, 0, -1):
    #This loop will start at 15 and count down by 1 each time
    print("counting down:",negative)
print("Final number:",negative)