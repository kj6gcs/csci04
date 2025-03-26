#Exercies 1 - define a function called "greeting" with no parameters and doesn't return a value.  Inside the function
#print the string "Hello! How are you doing?"  Call the greeting function you made

def greeting(): #defining greeting function
    print("Hello! How are you doing?") #printing string
    
greeting()

#Exercises 2 - Define a function called doMath that has no parameters and doesn't return a value.  In the function, write code that
#will create 3 variables: num1 num2 addition.  Initialize num1 to 15 num2 to 17.  Add num1 and num2 together and put the result into
#the addition variable.  Print the value of the addition variable.  Use your variables and let the computer do the math.  Call doMath

def doMath(): #define doMath function
    num1 = 15 #initialize num1 to 15
    num2 = 17 #initialize num2 to 17
    addition = num1 + num2 #using variables to do the math
    print(addition) #print the math
    
doMath() #calling doMath
