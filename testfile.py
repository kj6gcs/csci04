#*************************************************************************
# Your Name:           Robby Wideman
# Project Due Date:    02/26/2025
# Project Name:        Project 2: Metric Conversions
# CSCI-4: Intro to Programming
# Spring 2025
# Project Description: Program to convert metric measurements of height
# and weight into their English equivalents.
#*************************************************************************

# Write your code under this line*******************************************

print("\n~~Metric to English Height/Weight Converter~~")  # Fancy program title

conversions = []  # Storing future conversions here for later printing

while True:
    try:
        height_input = input("Enter height in Centimeters (or '0' to end): ").strip()
        
        if height_input == "":  # If they just press Enter, restart
            print("No conversions were performed. Restarting...\n")
            continue
        
        height = float(height_input)  
        if height == 0:
            break  # Exit loop if they enter 0

        # Loop until a valid weight is entered
        while True:
            weight_input = input("Enter weight in Kilograms (or '0' to end): ").strip()
            
            if weight_input == "":  # If they skip weight, show an error
                print("Error: You entered a height but did not enter a weight. Please try again.")
                continue  

            try:
                weight = float(weight_input)
                if weight == 0:
                    break  # Exit loop if 0 is entered
                break  # Valid weight, exit loop
            except ValueError:
                print("Invalid input. Please enter a valid number for weight.")

        if weight == 0:
            break  # Stop asking for input if 0 is entered

        # Conversion formulas
        resultHeight = height / 2.54  # Convert cm to inches
        resultWeight = weight * 2.2  # Convert kg to lbs

        # Store results
        conversions.append((resultHeight, resultWeight))

    except ValueError:
        print("Invalid input. Please enter a valid number for height.")

# Final results before exiting
print("\n~~Conversion Results~~")
if conversions:
    for resultHeight, resultWeight in conversions:
        feet = int(resultHeight // 12)  # Whole feet
        inches = int(resultHeight % 12)  # Remaining inches
        print(f"Height: {feet}'{inches}\", Weight: {round(resultWeight)} lbs")  
else:
    print("No conversions were performed.")  # If they exit immediately
