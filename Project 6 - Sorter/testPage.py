#Initialize function 
def initialize(list):
    #add exactly 10 0s to our list 
    for num in range(0,10): #Must repeat exactly 10 times 
        list.append(0)

#Function to fill list with inputted numbers 
def fillList(list): 
    #We need to be getting numbers from input, in a loop 
    #We need a way to stop EITHER when 0 is entered, or when 10 things have been entered
    #Use a while loop, use a boolean 
    done = False #As longs as this variable is False, our loop will repeat 
    #We'll say done is True once we are in a situation where we need to stop looping
    count = 0   #Count how many elements I've actually added to my list
    while not done: #Loop as long as done is not True (false)
        #Get a number as input (make sure to convert it to int)
        #If a 0 was entered OR we ran out of space in our list, we're done!
        #   done = True
        #Otherwise, add the input to our list 
        #   when we put input in our list, we need to find the right index 
        #   every time you put something in the list, increase your count
        return
        
#main function: where the program starts
def main():
    #make a list
    #initialize the list
    #   indices:  0  1  2  3
    numList = []   #Create the list, it's uninitialized, empty brackets
    #initialize the list 
    initialize(numList) #initialize list with 0s
    fillList(numList)   #Get user input, fill list with numbers 
    
    #print the unsorted list
    print("Unsorted",numList)
    #sort the list
    bubbleSort(list)
    #print the sorted list
    print("Sorted:",numList)
    
#First: you need to call main!
main()