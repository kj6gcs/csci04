#BubbleSort and Swap Function

def swap(leftIndex, rightIndex, list):
    print("before:",list)
    #For this to work, you need a way to remember what the left thing is BEFORE you destroy it
    temp = list[leftIndex]  #save the left element
    list[leftIndex] = list[rightIndex] #This will replace the left element, but I still have a copy in temp
    list[rightIndex] = temp
    print("after:",list)

def bubbleSort(list):
    #For bubblesort to work, need two nested loops
    #One loop will actually go through the list using an index
    #   that inner loop will actually do the sorting (compare things, swap them)
    #To keep sorting, to go through the list more than once, you must use another, outer loop 
    #   and put the inner sorting loop inside of that one 
    
    #First thing: how do we know when we're done sorting? If we get through the entire list 
    #   without swapping a single time, it must be sorted, because nothing is out of order
    swapped = True
    while swapped:  #As long as we have done at least one swap, keep repeating the sort 
        swapped = False #Start this assuming that we might not swap anything
        #If we get all the way to the end of this, and swapped is still false, we'll stop the sort 
        #Inside here, we need ANOTHER loop: a for loop. This loop will actually sort...
        #for currentIndex in range of numbers from the start to the end:
        #   Compare current thing to the next one 
        #   nextIndex = currentIndex + 1    #find where the next thing is, compared to the current one 
        #   if the element at currentIndex is greater than the thing at nextIndex...
        #       out of order, swap 
        #       swap(currentIndex, nextIndex, list)
        #       swapped = True
        
    return #return will end the function, will send back a value if you give it one 


#main function: where the program starts
def main():
    #make a list
    #initialize the list
    #   indices:  0  1  2  3
    numList = [7, 3, 2, 9]   #iniitializing this right here 
    #print the unsorted list
    print("Unsorted",numList)
    #sort the list
    bubbleSort(list)
    #print the sorted list
    print("Sorted:",numList)
    #swap(0,1,numberList)
    
#First: you need to call main!
main()

#******************************More notes on this from 04/28/2025 Class**********************************

#Initialize function(list):
def initialize(list):
    #adds exactly 10 0's to our list
    for num in range (0, 10): #must repeat exactly 10 times.
        list.append(0)

#main function: where the program starts:
def main():
    numList = []
    initialize(numList)
    print("Unsorted", numList)
    bubbleSort(list)
    print("Sorted:", numList)
    #swap(0, 1, numeberList)