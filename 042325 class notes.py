#Lists:
#Lists are collections of elements altogether, separate pieces of information treated as a single variable.
#To make a list:
#Indices: 0 1 2
numList = [1, 2, 3] #List of numbers w/3 elements.
print(numList)

#You can access individual elements of the list, using an index (or other ways).
#Print the first element of the list:
#The first element of any list (and the first thing of a string too) will be at index 0.
print("first", numList[0])

#There are different ways to change lists after they have been created.
#You can add new elements to a list using append()
#When you append something to a list, the new element(s) will always go at the END after all the others.
numList.append(5)
print("After append:", numList)
numList.append("you can really do whatever") #You can actually place different types of values (numbers, strings, etc) in a list, it's
#just not recommended because it can make the list confusing.
print("After", numList)

#How long is your list?  How many elements?  Use len()
length = len(numList) #Must assign it to something to use it like:
print("numList length:", length)

#To count how many of a specific value you have in your list...use list.count()
whateverList = ['a', 4, 5, 'b', "hello", 7, 7, 7]
countSeven = whateverList.count(7) #Must assign it to a variable to use it, like above
print("count", countSeven)

#Like strings, you can loop through elements in a list.
#There's a couple ways you can do this, for loops are the most useful
#If you want to do something to every element in a list... you can make a for loop
for thing in whateverList:
    print(thing) #Every time this loops repeats, it puts the next element of the list into the variable "thing".

print("**********************")   
#The other way of doing this is by using an index and a range of numbers.
#Make an empty list:
list = []
for index in range(0, 11):  #By doing this, you get a number (index) that counts up each time the loop repeats.
    list.append(index)
    print(list[index])
    print(list)
    
#******************************************************************************************
#Sorting Algorithms:
sortList = [7, 3, 2, 9]
