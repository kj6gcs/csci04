#Strings are actually lists of characters all together, treated as one big unit.
#Each individual character in a string hasa an index, which represents where that 
# character is within the string.
#Using an index, you can get any one character (or group of characters) from a string.
#Indices are needed to do certain things with strings (and also other stuff).
#Needed to get, alter, or otherwise do things to parts (or all) of a string.

#How do we use an index?
#stringName[index]  #This will let you do something with the character at the index 
# that you put in the [brackets]. (index must be a number)

#String variable:
someString = "Get the first letter!"
#Computers count starting from 0, so the index of the first character of a string will be 0.
first = someString[0]
print("first?", first)
#indices:   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
#chars:     G e t  t h e  f i r s t  l e t t e r!
another = someString[12]
print("t?", another)
#You can get the length of a string using len(string)
stringLength = len(someString)
print("length", stringLength)
print("second to last", someString[stringLength - 2])
#Because computers count from 0, the index of where something is might be a bit off from
#what you would expect.
#last = someString[20]
#print("last?", last)
#There is no index 21, even though there are 21 characters in the string.
#Because the first is at 0.
#If you try to go "out of bounds," to an index that isn't actually there, you will get errors.
#someString[9] = '!'
#print("after !", someString)

#How to use a loop on a string?
newStr = "Hey, it's raining outside"
#for variable in something:
    #do something with that variable.
for current in newStr:
    print(current)
    
    
#In order to do the cipher project (Project 5), you need to be able to figure out the number
#for each character in your string (number version of the letter).
#In Python, you can use ord().  ord() is a Python built-in function.
#charaacter variable
ch = 'A' #single quotation marks (') are for single characters.  (") is for more than one character.
#you can get errors if you don't follow this.
print("number?", ord(ch))   #ord gives us the numbewr version of this character.
cryptNum = ord(ch) + 3 #This will get the number of ch, add 3 to it.
print("cryptNum", cryptNum)
#Once you've changed the number of your char, change it back into a character.
#To make this back into a character....
print("encrypted?", chr(cryptNum))

ch = 'A'
ch = chr(ord(ch) + 3) #This will take the ch character, make it a number, change the number, then replpace the original,
                        #then make it a character again, then replace the original character.
                        

#It is recommended for our project to make a new string (encrypted string) by buildig it up from pieces of old string
#that you created.
#There's multiple ways to do this: concatenation (put/place things together)
hello = "Hello"
world = " World!"
both = hello + world #The plus symbol isn't doing addition here, it is placing strings together.
print(both)
world = world  + ch
print(world)
cryptString = ""
cryptString = cryptString + ch