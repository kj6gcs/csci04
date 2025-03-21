 #*************************************************************************
 # Your Name:           Robby Wideman
 # Project Due Date:    Wednesday, March 26th, 2025 by 2359 Hours
 # Project Name:        Project 3 - Dice Roller
 # CSCI-4:              Intro to Programming
 # Spring 2025
 # Project Description: A program which rolls random "dice" based on a
 # choice made by the user (which die to use).  The roll is made against
 # the program making it's own random roll, with the higher number rolled
 # being the winner.
 #*************************************************************************

#Write your code under this line*******************************************

#fist, the code to enable random:
import random

#let's welcome the players and explain the game.
print("\n~Robby's Random Dice Roller~")
print("\nFirst you'll pick which type of die to roll (D6, D8, 10. D12, D20, or D100).  Once you enter your")
print("choice, as well as how many rolls you wish to make (1-5), a random 'roll' of your die will be made against")
print("a roll of the same type and number of die by the computer.  The winner of the roll will be declared.\n")

#defining the valid dice options
valid_dice = [6, 8, 10, 12, 20, 100]


#have player pick type of die to roll
while True:
    while True:
        try:
            dieType = int(input("Enter the number of sides of your die/dice (enter '0' to end program): "))

        #condition check to see if player wishes to continue or exit:
            if dieType == 0:
                print("\nThanks for playing!  See you next time!!!\n")
                exit() #exits the program if player enters 0 for die type
        #error message if player enters incorrect number of die sides:    
            elif dieType not in valid_dice:
                print("Invalid die type entry.  Please choose from 6, 8, 10, 12, 20, or 100.")
                continue #stays in loop if invalid entry.
            break #exits loop if valid entry is made
        except ValueError:
            print("Invalid input.  Please enter a number.")

   #we're still in the main loop here.  if the player has made the correct die types, now we ask how many rolls:
    while True:
        try:
            numRolls = int(input("Enter the number of rolls you wish to make (1-5):"))
            if numRolls not in range(1,6): #generates error message if not within range
                print("Invalid selection.  Please enter a number between 1 and 5.")
                continue #keeps in loop to keep trying for valid selection
            break #exits loop if valid number of rolls is entered by player
        except ValueError: #generates error message if wrong input type
            print("Invalid input.  You must enter a number between 1-5. ")
            continue #stays in loop if invalid input, asks again for valid input

    #finally time to "roll" the dice!  these are the rolls for the player and the computer.
    player_rolls = [random.randint(1, dieType) for _ in range(numRolls)]
    computer_rolls = [random.randint(1, dieType) for _ in range(numRolls)]

    #calculating total amount of roll values for the player and the computer:
    player_total = sum(player_rolls)
    computer_total = sum(computer_rolls)

    #here we will display the results of the rolls for the player to see:
    print(f"\nYou rolled: {player_rolls} (Total: {player_total})")
    print(f"\nThe Computer rolled: {computer_rolls} (Total: {computer_total})\n")

    #declare the victor:
    if player_total > computer_total: #if player total is greater than computer's, player is the winner
        print("\n👑You win!👑\n")
        print("\\( ﾟヮﾟ)/🏆\n") #had to use a double back slash here to have a "proper" escape for the left side arm.  it would throw a warning
                                #previously, and using "r" for a raw string led to the \n not working just being printed.
    elif player_total < computer_total: #if less, then computer is winner
        print("The Computer Wins!\n")
        print("😭😭😭😭😭😭\n")
    else:
        print("👔It's a tie!👔\n")  #if equal, it's a tie!
        print("v(^_^)v\n")