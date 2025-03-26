#Functions
#Functions are reusable blocks of code you define in your program and can call to use anytime..
#In order to use a function, you must both define it and call it.
#Functions should be defined ABOVE the rest of your code.

#def functionName():
#    this is the code that will be part of your function.
#    anything not indented is not part of the function.
#    if you don't indent consistently, you will get errors.

def greet():    #this decides the name of the function, because of the def, we're creating it here.
    #this is indside the function because it is indented.
    print("Hello there!")
    
#When you start introducing functions, your program won't start with the first line of code.
#Code inside a function will not run until you call it
#You have to call the function from somewhere not inside the function itself
print("Starting the program!")
greet() #this will call the function.