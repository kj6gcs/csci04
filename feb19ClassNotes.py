#If you make a comment, you can write anything you want on that line, it will not hurt your program.
#Comments don't have to follow syntax rules/etc, because they are not code.

#Variables
#Variales are named locations used to store data, data in a variable can change anytime
#Before you use a variable, you must declare it
#In python, that means giving the variable a name, and, typically, a value.

#Data types: different kinds of data that can go into a variable, or be used for oter things.
#Integer: a number with no decimal point (whole number)
#float: a number with a decimal point.
#String: words, sequence of characters enclosed in double quotes (aka words/numbers/letters that aren't code)
#Character: A single letter, symbol, whatever--several characters together makes a string
#Boolean: a true or false value

#In most languages, to make a variable, you must decide it's type first.  It will stay that type pretty much for the rest of the
#program, and that type cannot change.  This is called strong typing.
#Python is different!  Python has weak typing.  This means that when you make a variable, it only needs a name and  a value.
#The value decides the type, and the type can change.

#To make a variable...
x = 10 #x is an interger type variable, because I put the number 10 in there.
name = "John Valdez" #name is a string type variable, because I put the string "John" in there.  A string literal.

#Because Python has week typing, data types of variables you already made can change (this is not an option in most other programming
#languages).
x = "Hello"         #By assigning a string to x, we change it's type to string.
                    #You can do this, but it's a bit weird, and should be avoided if possible.

#You can assign a literal, plain value to a variable, or you can assign the result of an expression.
#If you want to do math, for example, you can do that math on the right side of the = and that will put the
#result on the left side of the =
x = 5
x = x + 36 #this will calculate x (5) + 36 and replace x's value with that result (5+36=41).  X is then 41 moving forward.
#In order to see what we did, we need to print/get output, feedback.
print("x is:",x)

#EXERCISES
#1.
a = 10 #Assign the interger value 10 to a variable named a.
print(a)

#2.
b = 20.5 #Assign a float value 20.5 to a variable named b 
print(b)

#3.
greeting = "Hello, Python!" #Assign the string "Hello, Python!" to a variable named greeting.
print("greeting is:",greeting)

#4.
a = 15 #Assign 15 to a
b = 10 #Assign 10 to be
result1 = a + b
print("a + b =", a+b) #Do the math of calculating the sum of a and b.

#5.
a = 5 #Assign 5 to a
b = 20 #Assign 20 to b
result2 = a - b
print("a - b =", a-b) #Find the difference when b is subtracted from a.

#For output: making stuff show up on the screen, feed back, you use print().
#To get input, to send data from the outside into the program, you need to use input().
#In order to actually use the stuff typed in for input, you need to assign it to a variable.  Variables cannot start with numbers.
inputTest = input("Type whatever you want!") #Get input from the user
print("You typed:", inputTest) #Print the input

#When you take input this way, it automatically comes in as a STRING, even if you typed in a number.
#If you want to get a different type (such as a number), you need to specify.
inputNum = float(input("Type in a number. ")) #This will turn the input into a float (num with a decimal point)
print("Your number is:",inputNum)