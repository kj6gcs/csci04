#*************************************************************************
# Your Name:           Robby Wideman
# Project Due Date:    April 30th, 2025
# Project Name:        Project 6 - Sorter
# CSCI-4:              Intro to Programming
# Spring 2025
# Project Description: Program that reads up to 10 integers into a list,
# initializes it with zeros, allows early termination with 0, then sorts
# the list using a Bubble Sort function method in ascending or descending
# order.  Also, it can resort those same numbers, or even go again.  Plus
# fancy colors and stylizing!!!!
#*************************************************************************
#Write your code under this line******************************************

#Importing "time" in order to use it to stall exiting for a few seconds in a couple different places:
import time
# Importing "re" to help with centering ANSI text in the welcome and goodbye secions
import re

def center_ansi(text, width=80): # Helper code from ChatGPT to assist in properly centering specially formatted print lines using ANSI for stylizing.
    # Strip ANSI codes for measuring visible length
    ansi_escape = re.compile(r'\033\[[0-9;]*m')
    plain_text = ansi_escape.sub('', text)
    pad = (width - len(plain_text)) // 2
    return ' ' * pad + text


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
def rainbow_text(text, bold_indices=None):
    if bold_indices is None:
        bold_indices = []
    # Define a list of color codes (the basics for ANSI escape codes like I use for altering entire sections of text)
    # Since rainbow_text is it's own function, we're relisting the ANSI colors here as some vary, but we'll reuse the ones
    # I set previously in the global setting (like BOLD, ULINE (underline), and ITALIC)
    colors = [
        "\033[31m",  # Red
        "\033[33m",  # Yellow
        "\033[32m",  # Green
        "\033[36m",  # Cyan
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
    ]

    reset = "\033[0m"
    result = ""

    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        style = ""
        if i in bold_indices and char != " ":
            style = BOLD + ULINE + ITALIC  # This part will make sure in our acronym explainer line the first letters of the main words are using caps, italics, and underline
        result += color + style + char + reset + " "

    return result

def rainbow_text_no_spacing(text, bold_indices=None): #Rainbow text option.
    if bold_indices is None:
        bold_indices = []

    colors = [
        "\033[31m", "\033[33m", "\033[32m",  # Red, Yellow, Green
        "\033[36m", "\033[34m", "\033[35m",  # Cyan, Blue, Magenta
    ]

    result = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        style = BOLD + ULINE + ITALIC if i in bold_indices and char != " " else ""
        result += f"{color}{style}{char}\033[0m"  # no extra space added
    return result

# Defining required Functions
def check_for_quit(value): # This will be used later on as an option for the user to essentially quit at the number input stage of fillList().
    return value.strip().lower() in ['q', 'quit'] # Takes into account accidentally entered whitespace, upper/lower case, and options to quit.

def initialize(numList):
    # Adds exactly 10 zeroes to the variable numList.
    for _ in range(10): # Set our range target here.
        numList.append(0) # Appends these 0's to numList each time the loop runs (10 times), adding 0 to each index from 0 to 9 (10 total indices)

def fillList(numList):
    #Fills the list with up to 10 numbers or stops early if 0 is entered.
    print(rainbow_text("｡˚○ >>> ") + YELLOW + ITALIC + "Enter numbers (1 number per line, press ENTER after each number):" + RESET)
    count = 0
    while count < 10:
        user_input = input()
        if check_for_quit(user_input):
            print(rainbow_text("\n｡˚○｡˚○｡˚○    Goodbye!    ｡˚○｡˚○｡˚○｡˚○"))
            time.sleep(2.0) # This makes it wait 2 seconds before exiting the loop.
            exit() # Leaves the program completely.
        try:
            value = float(user_input)
            if value == 0:
                break
            numList[count] = value
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
    # Sorts the list using Bubble Sort (ascending or descending, as defined by user in main() function).
    n = len(lst)
    for i in range(n): #This sets the loop to repeat enough times (the length of the list, or in this case, the vairable n) to sort the list as directed.
        for j in range(0, n - i - 1): 
            #This is the portion where the actual swapping takes place.  The parameters essentially tell the program to ignore what has already been swapped and placed in the correct order.
            if (ascending and lst[j] > lst[j + 1]) or (not ascending and lst[j] < lst[j + 1]): # This part tells (based on user input) to sort in either
                                                                                               # ascending OR descending fashion.
                swap(j, j + 1, lst) #This part continues to call the swap function as long as our condition is True to swap list items (elements)

# Testing indices************************************************************************************************
# def print_indices(line):
#    print("\n📏 Character Index Map:\n")
#    for index, char in enumerate(line):
#        printable_char = repr(char)  # This will show spaces and special chars like ' '
#        print(f"{index:>3}: {printable_char}")
# bubble_line = "｡˚○  BUBBLE: Beautifully Unordered Batches Balanced by Logic Elegantly  ｡˚○"
# print_indices(bubble_line) 
# Leaving this test block in here just in case I need it again, won't show up in program though. ****************
# I was trying to figure out how to, in a rainbow_text print function line to stylized specific letters for the acromyn, but that was too much for right now lol.

# This is the heart of the program, putting together all the above-define functions/variables/etc.
def main():
    #Start of program instructions.
    print("\n\n") # Need the separate for centering the next line, and the one after it)
    welcome_line = "｡˚○  Welcome to Robby's 'Bubble' Sorter!  ｡˚○"
    print(center_ansi(rainbow_text_no_spacing(welcome_line))) #Calling our optional rainbot_text_no_spacing() from above.
    print()
    bubble_line = "\n｡˚○  BUBBLE: Beautifully Unordered Batches Balanced by Logic Elegantly  ｡˚○"
    print(center_ansi(rainbow_text_no_spacing(bubble_line)))
    print(ORANGE + ULINE + "\n\nInstructions:" + RESET)
    print(rainbow_text("｡˚○ >>> ") + RESET + BRIGHTBLUE + ITALIC +"Enter 10 numbers in any order, one line at a time, which you wish to sort" + RESET)
    print(rainbow_text("｡˚○ >>> ") + RESET + GREEN + "After sorting, you'll have the option to sort again or quit." + RESET)
    print(rainbow_text("｡˚○ >>> ") + RESET + ORANGE + ITALIC + "Chose (a) for ascending or (d) for descending sorting when prompted. (Pressing enter at this stage automatically sorts by ascending)" + RESET)
    print(rainbow_text("｡˚○ >>> ") + RESET + BRIGHTRED + BOLD + ITALIC + "Press 'q' when asked to quit.\n" + RESET)

    while True:
        numList = []
        initialize(numList)
        fillList(numList)

        while True:
            print(MAGENTA + ITALIC + "Unsorted:" + RESET, numList) #Prints the unsorted version of numList provided by the user.

            #This section let's the user sort the list in ascending or descending order.
            order = input(YELLOW + BOLD + "Sort in ascending or descending order? (a/d): " + RESET).strip().lower() 
            #The .strip() ignores any accidental whitespace input, .lower() makes the program recognize correct inputs in either upper or lower case.
            ascending = True if order == 'a' else False

            bubbleSort(numList, ascending) # Calling back the bubbleSort() function from above.
            # Determine color and label based on sort direction
            if ascending:
                color = CYAN
                direction_label = "(Ascending)"
            else:
                color = MAGENTA
                direction_label = "(Descending)"

            # Print the sorted list with a rainbow bubble and styling
            print(
                rainbow_text("｡˚○ >>> ")
                + RESET
                + BRIGHTBLUE + ITALIC + f"Sorted {direction_label}: " + RESET
                + rainbow_text("[")
                + color + ", ".join([str(round(num, 2)) for num in numList]) + RESET
                + rainbow_text("]")
            )

            # Converting numList to a string here in the output to change output colors (can't do with numbers)

            #Now we're going to get fancy and give users the option to resort their same list, create a new one, or just quit.
            next_action = input(MAGENTA + ITALIC + "\nWould you like to (r) re-sort the same list, (n) enter new numbers, or (q) quit? " + RESET).strip().lower()  
            #The .strip() ignores any accidental whitespace input, .lower() makes the program recognize correct inputs in either upper or lower case.
            if next_action == 'r':
                continue  #Keeps user in inner loop to re-sort the same list if they want.
            elif next_action == 'n':
                break      #Breaks user from the inner loop to restart with a new list if the want.
            elif next_action == 'q':
                print("\n\n")
                goodbye_line = "｡˚○｡˚○｡˚○    Goodbye!    ｡˚○｡˚○｡˚○｡˚○"
                print(center_ansi(rainbow_text_no_spacing(goodbye_line)))
                print()
                emoji_line = "🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉  ✨  🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉 🎉"
                print(center_ansi(emoji_line))
                time.sleep(2.0) # This makes it wait 2 seconds before exiting the loop.
                return      #Thanks for playing! (aka exit goodbye message)
            else:
                print(RED + BOLD + ITALIC + "Invalid choice. Please type 'r', 'n', or 'q'." + RESET) #User input error message if not a valid choice.


#Now we put it all together and let it rip!
main()
