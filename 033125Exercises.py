#1. Define two functions: start and newMath.
#newMath takes two integers as parameters: num1 and num2. The function doesn't return a value. In main, 
# create and initialize num1 and num2: both values should come from user input.
#Within the function, write code that will create a variable called subtraction. 
#Subtract num2 from num1 and put the result into the subtraction variable. 
#Print the value of the subtraction variable. 
#Remember to use your variables and let the computer do the math.
#In the start function, call the newMath function: make sure to give numbers/variables as parameters. What is printed, if anything?

#def start():
 #   num1 = int(input("Enter a number to subtract from: "))
  #  num2 = int(input("Enter a number to subtract from the first: "))
   # newMath(num1, num2)
    #return
    
#def newMath(num1, num2):
 #   subtraction = num1 - num2
  #  print(subtraction)
    
    
#Instructor example:
def newMath(num1, num2):
    subtraction = num1 - num2 #do some math, result goes into subtraction)
    print(subtraction)
    return

def start():
    #Start will set up the values/variables that go into newMath as parameters.
    num1 = float(input("First number? "))
    num2 = float(input("Second numner? "))
    newMath(num1, num2)
    return

#First thing not in a function, this goes first.
start()


