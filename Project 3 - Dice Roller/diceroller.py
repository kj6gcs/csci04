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
print("choice, as well as how many rolls you wish to make, a random 'roll' of your die will be made against")
print("a roll of the same type and number of die by the computer.  The winner of the roll will be declared.\n")

#have player pick type of die to roll
while True:
    dieType = int(input("Enter the number of sides of your die/dice (enter '0' to end program): "))

    #condition check to see if player wishes to continue or exit:
    if dieType == 0:
        print("\nThanks for playing!  See you next time!!!\n")
        exit()
    
    #tell them the type of die they chose:
    if dieType in [6, 8, 10, 12, 20, 100]:
        print(f"\nYou have chosen to roll a D{dieType}\n")
    #error message if player enters incorrect number of die sides:
    elif dieType not in [6, 8, 10, 12, 20, 100]:
        print("Invalid die type entry.  Please make a valid die type selection!")
        continue

    #if valid entry, move on to number of rolls:
    break

while True:
    numRolls = int(input("Enter the number of rolls want you to make (1-5): "))
    #error message if player enters incorrect number of die sides:

    #tell them how many rolls they've chosen to make
    if numRolls in [1, 2, 3, 4, 5]:
        print(f"\nYou are rolling a D{dieType} a total of {numRolls} times.  Good luck!\n")
    elif numRolls not in [1, 2, 3, 4, 5]:
        print("Invalid number of rolls.  Please enter a valid number of rolls!")
        continue

    #if valid entry, exit loop and calculate rolls:
    break