 #*************************************************************************
 # Your Name:           Robby Wideman
 # Project Due Date:    02/26/2025
 # Project Name:        Project 2: Metric Conversions
 # CSCI-4: Intro to Programming
 # Spring 2025
 # Project Description: Program to convert metric measurements of height
 # and weight into their English equivalants.
 #*************************************************************************

#Write your code under this line*******************************************

print("\n~~Metric to English Height/Weight Converter~~") #fancy program title so people know what program they're in and what it does =)

conversions = [] #storage list (like an array in JavaScript) to hold results for future conversions for later printing

while True: #this starts the loop with the keyword "while"
    try: #"try:" is used to find defined exceptions.  Before I added this, if you simply hit "enter" the program would end and not perform conversions.  Like a program crash.
        height = float(input("Enter height in Centimeters (or '0' to end): ")) #input for height, given in cm
        if height == 0: #sets condition to break/exit the loop
            break #exits loop if "0" is entered.

        weight = float(input("Enter weight in Kilograms (or '0' to end): ")) #input for weight, given in kg
        if weight == 0: #sets condition to break/exit the loop
            break #exits loop if "0" is entered.

#formula to calculate conversion & make it clean looking:
        resultHeight = height / 2.54 #this calculates the height conversion from metric to English
        resultWeight = weight * 2.2 #this calculates the weight conversion from metric to English

#store results to conversions container:
        conversions.append((resultHeight, resultWeight)) 
        #the ".append" chained to the conversions variable tells the program to store the entered results into the conversions list (written at top of code)

    except ValueError: #this creates an exception to go along with the "try:" conditions.  If a number/0 isn't entered, the user receives the below message
        print("You must enter a number or enter '0' to end.  Picking up from where you left off...\n")
        continue #this continues the program from right before where the user entered an invalid input, allowing their work to not be lost before conversions.

#final results are printed via the following:
print("\n~~Conversion Results~~") #fancy title to let them know they're getting their input as converted values
if conversions: #basically tells the program "if there are values stored in conversions, do the following"
    for resultHeight, resultWeight in conversions: #tells the program where to pick data from and which variables to pull that data from within the conversions list
        feet = int(resultHeight // 12) #this gives us the total feet (English) as a whole number
        inches = int(resultHeight % 12) #this gives us the remaining inches (English) after the whole number in feet
        print (f"Height in the English System is: {feet}'{inches}\", Weight in the English System is: {int(resultWeight)} pounds")
        #the command above will take the results from the previous calculations and print them in a neat format of feet' inches" and weight pounds.
else:
    print("No conversions were performed.") #if the user quits the program at the start by entering a "0," this command will run.
