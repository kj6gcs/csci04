#import random library for program
import random


randomNum = int(input("Enter a number."))

#you can make random numers with variables as the range
min = 50
max = 100
randomNum = random.randint(min,max)
print("Second Roll:",randomNum)

#how to validate input (make sure data someone puts into your program is what it's supposed to be)?
#let's say you want to get 0 as an input.  just 0.  no other numers allowed.
#first let's take input
zero = int(input("Please type 0!"))

#if-then to check input
if zero == 0:               #if input is exactly 0, then...
    print("You typed:",zero)
else:                       #if the input is literally anything other than 0 then...
    print("Not zero!!! Please try again.")

#using a boolean (True or False)
isValid = False
if isValid:
    print("Valid!")
else:
    print("Not valid!")