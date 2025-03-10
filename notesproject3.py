#################     Simple input validation checking      ####################
userInput = int(input("Type an allowed number (allowed numers are 1 and 10)"))
#Handle the allowed numbers:
if userInput == 1:
    print("Allowed! Doing things for 1...")
elif userInput == 10:
    print("Allowed!  Doing things for 10...")
else:
    print("Invalid input, not allowed!  Please try again.")