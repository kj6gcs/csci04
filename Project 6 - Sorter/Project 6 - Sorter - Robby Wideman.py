#*************************************************************************
# Your Name:           Robby Wideman
# Project Due Date:    April 30th, 2025
# Project Name:        Project 6 - Sorter
# CSCI-4:              Intro to Programming
# Spring 2025
# Project Description: Program that reads up to 10 integers into a list,
# initializes it with zeros, allows early termination with 0, then sorts
# the list using a hand-coded Bubble Sort in ascending or descending order.
#*************************************************************************

#I like some color in my terminal.  Were going to use ANSI escape codes for colors:
RED         = "\033[91m"
GREEN       = "\033[92m"
YELLOW      = "\033[93m"
CYAN        = "\033[96m"
BLUE        = "\033[34m"
BRIGHTBLUE  = "\033[94m"
BRIGHTRED   = "\033[91m"
ORANGE      = "\033[38;5;208m"
MAGENTA     = "\033[35m"
ITALIC      = "\033[3m"     # Adding some "style" to it!
BOLD        = "\033[1m"    # BOLD - for when you want your text to stand out!
RESET       = "\033[0m"     # This has to be used after each time the text is altered to reset the text back to it's baseline.
ULINE       = "\033[4m"     # Setting an underline style option.

# I also wanted to do something different for the welcome message.  I remember as a kid blowing bubbles (even those hard to blow
# plastic/chemical bubbles from a squeeze tube!) and seeing a rainbow of colors.  So, for the the first line of the welcome message,
# I got some help from ChatGPT to create a function which would automatically alternate colors of a specific line for each character
# in order to invoke some of my nostalgia in others.  I know "Bubble" isn't quite referring to all that, but it's the first thing
# that comes to my mind when I hear it.  But, I didn't want to have to add COLOR + COLOR + COLOR + COLOR inbetween each individual
# character, so:
def rainbow_text(text):
    # Define a list of color codes (the basics for ANSI escape codes like I use for altering entire sections of text)
    colors = [
        "\033[31m",  # Red
        "\033[33m",  # Yellow
        "\033[32m",  # Green
        "\033[36m",  # Cyan
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
    ]

    reset = "\033[0m"  # Reset color
    color_index = 0    # Start at first color

    for char in text:
        color = colors[color_index % len(colors)]  # Cycle colors
        print(color + char + reset, end="")        # Print each character
        color_index += 1

    print()  # Move to a new line after printing


# Defining required Functions
def initialize(numList):
    #Adds exactly 10 zeroes to the variable numList.
    for num in range(0,10):
        numList.append(0)

def fillList(numList):
    #Fills the list with up to 10 numbers or stops early if 0 is entered.
    print(rainbow_text("｡˚○"), YELLOW + ITALIC + ">>>Enter numbers (1 number per line, press ENTER after each number):")
    count = 0
    while count < 10:
        try:
            value = int(input())
            numList[count] = value
            if value == 0:
                break
            count += 1
        except ValueError:
            print(RED + BOLD + ITALIC + "Invalid input. Please enter a number." + RESET)

def swap(leftIndex, rightIndex, lst): #This fun function does the actual swapping of the numbers.  It makes sure to remember what the left number is BEFORE
                                      #it's destroyed by the move!
    #Swaps the elements at the given indices.
    temp = lst[leftIndex]
    lst[leftIndex] = lst[rightIndex]    #This replaces the left element, but leaves a copy in the temp variable.
    lst[rightIndex] = temp

def bubbleSort(lst, ascending=True): #ascending=True is a fall back in case the user doesn't select either ascending or descending when prompted.
    #Sorts the list using Bubble Sort (ascending or descending, as defined by user in main() function).
    n = len(lst)
    for i in range(n): #This sets the loop to repeat enough times (the length of the list, or in this case, the vairable n) to sort the list as directed.
        for j in range(0, n - i - 1): #This is the portion where the actual swapping takes place.  The parameters essentially tell the program to ignore
                                      #what has already been swapped and placed in the correct order.
            if (ascending and lst[j] > lst[j + 1]) or (not ascending and lst[j] < lst[j + 1]): #This part tells (based on user input) to sort in either
                                                                                               #ascending OR descending fashion.
                swap(j, j + 1, lst) #This part continues to call the swap function as long as our condition is True to swap list items (elements)

#This is the heart of the program, putting together all the above-define functions/variables/etc.
def main():
    #Start of program instructions.
    rainbow_text("\n｡˚○ Welcome to the Bubble Sorter! ｡˚○\n") # Starting off with our special rainbow_text function!
    print(MAGENTA + ULINE + "Instructions:" + RESET)
    print(BRIGHTBLUE + "｡˚○  " + GREEN + ITALIC +">>> Enter 10 numbers in any order, one line at a time, which you wish to sort" + RESET)
    print(BRIGHTBLUE + "｡˚○  " + BRIGHTRED + ">>> Enter 0 at any time to sort early." + RESET)
    print(BRIGHTBLUE + "｡˚○  " + GREEN + ">>> After sorting, you'll have the option to sort again or quit." + RESET)
    print(BRIGHTBLUE + "｡˚○  " + ORANGE + ITALIC + ">>> Chose (a) for ascending or (d) for descending sorting when prompted. (Pressing enter at this stage automatically sorts by ascending)" + RESET)
    print(BRIGHTBLUE + "｡˚○  " + BRIGHTRED + BOLD + ITALIC + ">>> Press 'q' when asked to quit.\n" + RESET)

    while True:
        numList = []
        initialize(numList)
        fillList(numList)

        while True:
            print(MAGENTA + ITALIC + "Unsorted:" + RESET, numList) #Prints the unsorted version of numList provided by the user.

            #This section let's the user sort the list in ascending or descending order.
            order = input(YELLOW + BOLD + ULINE + "Sort in ascending or descending order? (a/d): " + RESET).strip().lower() #The .strip() ignores any accidental whitespace input, .lower() makes
                                                                                            #the program recognize correct inputs in either upper or lower case.
            ascending = True if order == 'a' else False

            bubbleSort(numList, ascending)
            print(BRIGHTBLUE + ITALIC + "Sorted: " + RESET, numList)

            #Now we're going to get fancy and give users the option to resort their same list, create a new one, or just quit.
            next_action = input(MAGENTA + ITALIC + "\nWould you like to (r) re-sort the same list, (n) enter new numbers, or (q) quit? " + RESET).strip().lower()  #The .strip() ignores any 
                                                                                                                                        #accidental whitespace input, .lower() 
                                                                                                                                        #makes the program recognize correct inputs
                                                                                                                                        #in either upper or lower case.
            if next_action == 'r':
                continue  #Keeps user in inner loop to re-sort the same list if they want.
            elif next_action == 'n':
                break      #Breaks user from the inner loop to restart with a new list if the want.
            elif next_action == 'q':
                rainbow_text("｡˚○｡˚○｡˚○    Goodbye!    ｡˚○｡˚○｡˚○｡˚○")
                return      #Thanks for playing! (aka exit goodbye message)
            else:
                print(RED + BOLD + ITALIC + "Invalid choice. Please type 'r', 'n', or 'q'." + RESET) #User input error message if not a valid choice.

#Now we put it all together and let it rip!
main()
