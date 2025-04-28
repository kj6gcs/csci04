#More on lists
#Specifically, Operations.

#Make a list
numbers = [1, 2, 3, 4, 5] #Initialized, list, contains numbers (specifically integers)

#list.append(value)
#Append adds the value in parentheses () to the end of your list.
numbers.append(10)
numbers.append('some words') #this works, too, don't mix types though.

print("After append: ", numbers)

#list.count(value)
#Counts up how many times the value in the parentheses appears in the list.
#Importantly: this RETURNS the number.  In order to use the count you get, you must do something with is.
print("Count: ", numbers.count(5)) #by doing this i can see the count in this print,
#but i don't have the count.  it's not in a variable.  To use it later, I'd have to run .count() again.

#adding some more 5's.
numbers.append(5)
numbers.append(5)
numbers.append(5)

countFive = numbers.count(5)
print("list + more 5's", numbers)
print("How many 5's?: ", countFive)

#numbers.append(2, 5, 7, 9) #This function/variable can only take 1 thing at a time (append), this specifically causes an error.
#You can use append in a loop to add more than one thing, but if you already have a list to add...
#list.extend(otherList)
#Like appened, this adds the values in parentheses onto the end of your list.  But,
#unlike append, this adds entire lists, rather than single values.
#numbers.extend(2, 5, 7, 9)   #This also doesn't work, your values must all be in a list.
newList = [2, 5, 7, 9]  #newList contains more numbers.
numbers.extend(newList)
print("exdended?", numbers)
#indices:   0  1  2  3  4  5        6        7  8  9  10 11 12 13 (indexes always start at 0!)
#elements: [1, 2, 3, 4, 5, 10, 'some words', 5, 5, 5, 2, 5, 7, 9]

#Sometimes you may need to find where soething is in your list, like a specific value
#One way to do this...


#list.index(value)
#Returns the index (location) of the first element in you list that has the
#value in parentheses ()
#Let's say I needed to find the first place that 7 appears in my list...
sevenIndex = numbers.index(7) #Finds where the first spot the value 7 appears.
print("index: ", sevenIndex)
print("that thing at index: ", numbers[sevenIndex])

print("where's 5? ", numbers.index(5)) #This only tells me where the FIRST 5 is, not the others.

#list.insert(index, value)
#Rather than just adding stuff onto the end of the list, insert will put things
#at the specific index you put.
numbers.insert(sevenIndex, 999) #Put the number 999 at the index sevenIndex
print("after insert:", numbers)

                                                                    #v len() - 1 gets index of last item in list.
#indices:   0  1  2  3  4  5        6        7  8  9  10 11   12 13 14 (indexes always start at 0!)
#elements: [1, 2, 3, 4, 5, 10, 'some words', 5, 5, 5, 2, 5, 999, 7, 9]
#This adds new stuff WITHOUT replacing anything.

#len(list)
#This will return how long the list in parentheses is (counts all the elements)
print("numbers length: ", len(numbers)) #If I wanted to use this somewhere else, I would need
#to put in in a variable or do len() again.

