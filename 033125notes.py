#To make a function, first define it, then call it.
#When you define functions, they should go at the top of your program.
#You should deefine all of your functions before you start calling them.
def helloName(yourName): #This would send in your name as a parameer.
    yourName = "Robby"  #This is a local variable.  It only exists inside the function.
    print("Hello,", yourName)
    #If I want the changes to the yourName variable to "stick," then I need to return it.
    #Returning a value sends it out of the function to whatever called it.
    return yourName#this ends the function immediately (after return).  If no return, it ends when it runs out of code.

def SomeOtherFunc():
    yourName = "John"
    #This function calls the helloName function for the sake of demonstration.
    yourName = helloName(yourName)
    print(yourName)
    print("Global var is:", globalTest)
    return
#Everything else goes below the functions.
#In order to make a function run and actually do something,
#you must call it.
#Making a variable to print.
#When you put a variable outside of a function outside of a function in Python, it's considered a global variable.
#Meaning it's supposed to exist everywhere.

globalTest = "global!"
SomeOtherFunc()
#yourName = "blank" #This name can be seen by functions, but it CANNOT be changed by them unless you use a special keyword.
#helloName(yourName) #this is all that's required to call a function.  This calls the "helloName" function.
#print(yourName)

###################################
#Global variables...
#Technically, any variable created OUTSIDE of a function is global, so all functions can see i,
#except they can't change it.  Unless they use the keyword "global"
def modify():
    global car  #This draws in the variable from outside the function (in main) and let's it change said variable.
    car = car + " Mustang"
    return

car = "Ford"
#The above variable is global because it is not inside a function.
modify()
print("You new car is:", car)