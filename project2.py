 #*************************************************************************
 # Your Name:           Robby Wideman
 # Project Due Date:    02/26/2025
 # Project Name:        Project 2: Metric Conversions
 # CSCI-4: Intro to Programming
 # Spring 2025
 # Project Description: Program to convert metric measurements of height
 # and weight into their english equivilants.
 #*************************************************************************

#Write your code under this line*******************************************

print("\n~~Metric to English Height/Weight Converter~~") #fancy program title so people know what program their in and what it does =)

conversions = [] #storing future conversions here for later printing

while True:
    height = float(input("Enter height in Centimeters (or '0' to end): ")) #input for height, given in cm
    if height == 0:
        break

    weight = float(input("Enter weight in Kilograms (or '0' to end): ")) #input for weight, given in kg
    if weight == 0:
        break

#formula to calculate conversion & make it clean looking:
    resultHeight = height / 2.54 #this calculates the height conversion from metric to English
    resultWeight = weight * 2.2 #this calculates the weight conversion from metric to English

#store results to conversions container:
    conversions.append((resultHeight, resultWeight))

#final results are printed here:
print("\n~~Conversion Results~~")
if conversions:
    for resultHeight, resultWeight in conversions:
        feet = int(resultHeight // 12) #this gives us the total feet (English) as a whole number
        inches = int(resultHeight % 12) #this gives us the remaining inches (English) after the whole number in feet
        print (f"Height in the English System is: {feet}'{inches}\", Weight in the English System is: {int(resultWeight)} pounds")
else:
    print("No conversions were performed.")
