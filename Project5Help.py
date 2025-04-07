#Functions should all be defined aboe the rest of your code.
#Functions must be defined before they get called!
def encrypt():
    #This should have parameters, avoid globals.
    #You NEED a loop, for loop, to go through the string.
    #encrypt each character with ord and by adding the shift to each char
    #once you're done, you need to return the result
    return "test" #we will want to return the encrypt function here

#We're trying to make a program that encrypts strings.
#Before I can encrypt any strings, I'm going to need a string and a number
#The string will be what gets encrypted.
#The number will be what get's added to each character to encrpyt.


#FIRST STEP OF PROGRAM: CREATE VARIABLES
message = input("Please ype the string you'd like to encrypt, then press ENTER: ")
shift = int(input("Please type the shift value: ")) #Must take shift as int to work later
#Inputs in python are always STRINGS.  to make them not strings, conver to anooher type
#To test, print the inputs:
print("message: ", message, "shift: ", shift)
#If you want to check the type of something, you can:
#print(type(shift))

#SECOND STEP: Create encrypt function
#Encrypt the message:
#encrypt will need PARAMETERS.  (message shift)
message = encrypt() #This will take the message/shift value and encrypt the message,
                    #sends the new message back.
#After encryption is done, print the message
print("Encrypted text: ", message)

