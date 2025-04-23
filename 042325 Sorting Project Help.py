#                 SORTING LIST EXAMPLE      

def swap(leftIndex, rightIndex, list):
    print("before:", list)
    #For this to work, you need to "remember" what the left thing is BEFORE you destroy it.
    temp = list[leftIndex] #saves the left element
    list[leftIndex] = list[rightIndex] #this will replace the left element, but there's still a copy in temp
    list[rightIndex] = temp
    print("after:", list)

def bubbleSort(list):
    #For bubblesort to work, need two for loops (i.e. a loop that loops a nested loop within it)
    #One loop will actually go through the list using an index.
    #That inner loop will actually do the sorting. (compare things, swap them, etc).
    #To keep sorting, to go through the list more than once, you must use another outer loop
    #   and put the inner sorting loop inside of that one.
    
    #First thing: how do we know when we're done sorting?  If we get through the entire list
    #   without swapping a single time, it must be sorted, because nothing is out of order.
    swapped = True
    while swapped:  #As long as we have done at least one swap, keep repeating the sort
        swapped = False #start this assuming we might not swap anything.
        #If we get all the way to the end of this and swapped is still false, we'll stop the sort.
        #Inside here, we need ANOTHER loop: a for loop.  This loop will actually sort...
        #For currentIndex in range of numbers from the start of the list to the end:
        #   Compare current thing to the next one.   
        #   nextIndex = currentIndex +1  #find where the next thing is, compaed to the current one.
        #   If the element at currentIndex is greater than the thing at the nextIndex...
        #   out of order, swap
        #   swap(CurrentIndex, nextIndex, list)
        # swapped = True (this will trigger the while loop it's in)
    return #Return will end the function, will send back a value if you give it one.              

#main function where the program starts.
def main():
    #make a list
    #initialize the 
    numberList = [7, 3, 2, 9] #initializingthis right here
    #print the unsorted list
    print("Unsorted:", numberList)
    #sort the list
    bubbleSort(list)
    #print the sorted list
    print("Sorted:", numberList)
    swap(0, 1, numberList)
    
    
#First, you need to call main()!
main()