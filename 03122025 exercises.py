import random               #import random library
ok = input("Type 'ok' to generate a nuber between 1 and 6!") #ask for specific string input to generate random number
ranNum = random.randint(1,6) #pulls random number 1-6 and assigns it to ranNum

if  ok == "ok": #if statement to check if user entered string correctly
    print(ranNum)   #if so, random number 1-6 will be generated
else:   #else statement for anything entered other than "ok"
    print("Not a valid entry!") #tells the user they entered an invalid entry




allowed = False         #setting allowed to false
validPass = "password"  #setting system password

while allowed == False:
    entry = input("Enter password: ")   #take input for a password
    if entry == validPass:  #condition to see if password is correct
            print("Access granted!")    #result if password matches
            allowed = True
    else:
        print("Access denied!  Please try again!") #result if password is incorrect